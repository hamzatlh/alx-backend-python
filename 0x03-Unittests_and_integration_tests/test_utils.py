#!/usr/bin/env python3
""" Parameterize Unittests """
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map
from typing import Any, Tuple, Dict
from utils import get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    This is a class that contains unit tests for the,
    utils.access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict[str, Any],
                               path: Tuple[str], expected: Any) -> None:
        """ nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a", "a"),
        ({"a": 1}, ("a", "b"), "b", "b")
    ])
    def test_access_nested_map_exception(self, _, nested_map, path, expected):
        """
        This is a context manager that checks,
        if the function raises a KeyError with the,
        expected message for each input
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(expected))


class TestGetJson(unittest.TestCase):
    """Test the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns the expected result"""
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test the memoize decorator"""

    def test_memoize(self):
        """Test that memoize caches the result of a function call"""

        # Define a test class with a method and a property
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create an instance of the test class
        test_obj = TestClass()

        # Use patch to mock the a_method function
        with patch.object(TestClass, "a_method") as mock_method:
            # Configure the mock method to return 42
            mock_method.return_value = 42

            # Call the a_property twice
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            # Test that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Test that the mock method was called only once
            mock_method.assert_called_once()
