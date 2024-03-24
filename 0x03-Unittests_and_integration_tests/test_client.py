#!/usr/bin/env python3
""" Parameterize and patch as decorators """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from parameterized import parameterized_class
from client import GithubOrgClient
from unittest.mock import PropertyMock
import requests
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get):
        """Test that GithubOrgClient.org returns the correct value"""
        mock_get.return_value = {"name": org_name}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {"name": org_name})
        mock_get.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """
        Test that GithubOrgClient._public_repos_url returns the correct URL
        """
        # Define a test payload for the organization
        test_payload = {
                "repos_url": "https://api.github.com/orgs/google/repos"
                }

        # Use patch as a context manager to mock the org property
        with patch.object(
                GithubOrgClient, "org", new_callable=PropertyMock
                ) as mock_org:
            # Configure the mock property to return the test payload
            mock_org.return_value = test_payload

            # Create an instance of the GithubOrgClient,
            # class with a test organization name
            client = GithubOrgClient("google")

            # Test that the _public_repos_url method returns the expected URL
            self.assertEqual(
                    client._public_repos_url, test_payload["repos_url"]
                    )

    @patch("client.get_json")
    @patch.object(GithubOrgClient, "_public_repos_url",
                  new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test that GithubOrgClient.public_repos,
        returns the correct list of repos
        """
        # Define a test payload for the repos
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]

        # Configure the mock methods to return the test payloads
        mock_get_json.return_value = test_payload
        mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/google/repos"
                )

        # Create an instance of the GithubOrgClient class,
        # with a test organization name
        client = GithubOrgClient("google")

        # Test that the public_repos method returns the expected list of repos
        self.assertEqual(client.public_repos(), ["repo1", "repo2"])
        # Test that the mocked property and the mocked get_json was called once
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand(
            [
                ({"license": {"key": "my_license"}}, "my_license", True),
                ({"license": {"key": "other_license"}}, "my_license", False)
                ]
    )
    def test_has_license(self, repo, license_key, expected_output):
        """
        Test that GithubOrgClient.has_license returns the correct boolean
        """
        # Create an instance of the GithubOrgClient class,
        # with a test organization name
        client = GithubOrgClient("google")

        # Test that the has_license method returns the expected boolean
        self.assertEqual(client.has_license(repo, license_key),
                         expected_output)


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up the tests"""
        cls.get_patcher = patch.object(requests, 'get')

        # Start the patcher
        cls.mock_get = cls.get_patcher.start()

        # Set the side_effect of .json() to return the correct fixtures
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload,
            cls.expected_repos, cls.apache2_repos
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down the tests"""
        # Stop the patcher
        cls.get_patcher.stop()
