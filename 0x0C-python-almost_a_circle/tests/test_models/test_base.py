import unittest
import json
from models.base import Base

class TestBase(unittest.TestCase):

    def test_init_with_id(self):
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_init_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string(self):
        obj = Base(1)
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{'id': 1}]), '[{"id": 1}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string('[]'), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{'id': 1}])

    def test_create_rectangle(self):
        r = Base.create(**{'id': 1, 'width': 3, 'height': 4, 'x': 5, 'y': 6})
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_create_square(self):
        s = Base.create(**{'id': 2, 'size': 7, 'x': 8, 'y': 9})
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 8)
        self.assertEqual(s.y, 9)

    def test_load_from_file(self):
        r = Base.create(**{'id': 1, 'width': 3, 'height': 4, 'x': 5, 'y': 6})
        Base.save_to_file([r])
        instances = Base.load_from_file()
        self.assertEqual(len(instances), 1)
        self.assertIsInstance(instances[0], Base)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[0].width, 3)
        self.assertEqual(instances[0].height, 4)
        self.assertEqual(instances[0].x, 5)
        self.assertEqual(instances[0].y, 6)

if __name__ == '__main__':
    unittest.main()
