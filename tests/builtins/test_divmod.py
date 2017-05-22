from .. utils import TranspileTestCase, BuiltinFunctionTestCase, BuiltinTwoargFunctionTestCase


class DivmodTests(TranspileTestCase):
    pass


class BuiltinDivmodFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["divmod"]

    not_implemented = [
        'test_bool',
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_dict',
        'test_float',
        'test_frozenset',
        'test_int',
        'test_list',
        'test_None',
        'test_NotImplemented',
        'test_range',
        'test_set',
        'test_slice',
        'test_str',
        'test_tuple',
    ]


class BuiltinTwoargDivmodFunctionTests(BuiltinTwoargFunctionTestCase, TranspileTestCase):
    functions = ["divmod"]

    not_implemented = [
        'test_bool_complex',

        'test_bytearray_complex',
        'test_bytearray_frozenset',

        'test_bytes_class',
        'test_bytes_complex',

        'test_class_complex',
        'test_class_None',
        'test_class_NotImplemented',
        'test_class_range',

        'test_complex_bytearray',
        'test_complex_range',

        'test_dict_class',
        'test_dict_complex',
        'test_dict_frozenset',

        'test_float_complex',

        'test_frozenset_complex',

        'test_int_complex',

        'test_list_complex',

        'test_None_class',
        'test_None_complex',

        'test_NotImplemented_class',
        'test_NotImplemented_complex',

        'test_range_complex',
        'test_range_frozenset',

        'test_set_complex',

        'test_slice_class',
        'test_slice_complex',

        'test_str_complex',

        'test_tuple_complex',
    ]
