from unittest import TestCase, main

class TestingStringMethods(TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual('bradBuRY'.upper(),'BRADBURY')

    def test_isupper(self):
        self.assertTrue('APPLE'.isupper())
        self.assertFalse('banana'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(),['hello','world'])
        with self.assertRaises(TypeError):
            s.split('l')

if __name__ == '__main__':
    main()