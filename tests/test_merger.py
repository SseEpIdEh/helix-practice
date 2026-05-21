import pytest
from config.merger import merge_configs

# F2P Tests - these FAIL on buggy code, PASS on fixed code

def test_deep_merge_nested_dicts():
    base = {"db": {"host": "localhost", "port": 5432}}
    override = {"db": {"port": 5433, "name": "prod"}}
    result = merge_configs(base, override)
    assert result == {"db": {"host": "localhost", "port": 5433, "name": "prod"}}

def test_deeply_nested_three_levels():
    base = {"a": {"b": {"c": 1, "d": 2}}}
    override = {"a": {"b": {"c": 99}}}
    assert merge_configs(base, override) == {"a": {"b": {"c": 99, "d": 2}}}

# PASS_TO_PASS Tests - these PASS on both buggy and fixed code

def test_shallow_merge():
    base = {"a": 1, "b": 2}
    override = {"b": 3, "c": 4}
    assert merge_configs(base, override) == {"a": 1, "b": 3, "c": 4}

def test_empty_override():
    base = {"x": 1}
    assert merge_configs(base, {}) == {"x": 1}

def test_empty_base():
    assert merge_configs({}, {"x": 1}) == {"x": 1}
