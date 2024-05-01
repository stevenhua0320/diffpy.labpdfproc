import argparse

import pytest

from diffpy.labpdfproc.tools import set_wavelength

params2 = [
    ([None, None], [0.71]),
    ([None, "Ag"], [0.59]),
    ([0.25, "Ag"], [0.25]),
    ([0.25, None], [0.25]),
]


@pytest.mark.parametrize("inputs, expected", params2)
def test_set_wavelength(inputs, expected):
    expected_wavelength = expected[0]
    actual_args = argparse.Namespace(wavelength=inputs[0], anode_type=inputs[1])
    actual_wavelength = set_wavelength(actual_args)
    assert actual_wavelength == expected_wavelength


params3 = [
    ([None, "invalid"]),
    ([0, None]),
    ([-1, "Mo"]),
]


@pytest.mark.parametrize("inputs", params3)
def test_set_wavelength_bad(inputs):
    with pytest.raises(ValueError):
        actual_args = argparse.Namespace(wavelength=inputs[0], anode_type=inputs[1])
        actual_args.wavelength = set_wavelength(actual_args)
