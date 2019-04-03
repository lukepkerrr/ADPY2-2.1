import unittest
from app import App
from helpers.config import Config
from sys import platform


class TestConfig(unittest.TestCase):
    @unittest.skipUnless(platform.startswith('linux'), 'Only for linux')
    def test_windows_system_disk_err(self):
        self.assertRaises(EnvironmentError, Config.get_windows_system_disk)

    def test_get_windows_system_disk(self):
        self.assertIsInstance(Config().get_windows_system_disk(), str)

    def test_get_verbosity_level(self):
        self.assertIsInstance(Config().get_verbosity_level(), str)

    def test_get_verbosity_level_with_console(self):
        self.assertEqual(Config().get_verbosity_level('console'), 10)

    def test_get_verbosity_level_with_none(self):
        self.assertEqual(Config().get_verbosity_level(None), 'critical, error, warning, info, debug')

    def test_get_verbosity_level_with_num(self):
        self.assertEqual(Config().get_verbosity_level(1), 20)

    def test_get_verbosity_level_with_text(self):
        self.assertEqual(Config().get_verbosity_level(1, 'text'), 'info')

    def test_init_env_config_path(self):
        self.assertEqual(len(Config().init_env_config_path()), 5)

    def test_init_config_file(self):
        self.assertEqual(Config().config_file, 'testapp.yaml')


class TestApp(unittest.TestCase):
    def test_app(self):
        temp_var = App()
        self.assertTrue(isinstance(temp_var.config, Config))


if __name__ == '__main__':
    unittest.main()