import pytest

import numpy as np

import xgi
from xgi.exception import XGIError


def test_random_layout():

    H = xgi.random_hypergraph(10, [0.2], seed=1)

    # seed
    pos1 = xgi.random_layout(H, seed=1)
    pos2 = xgi.random_layout(H, seed=2)
    pos3 = xgi.random_layout(H, seed=2)
    assert pos1.keys() == pos2.keys()
    assert pos2.keys() == pos3.keys()
    assert not np.allclose(list(pos1.values()), list(pos2.values()))
    assert np.allclose(list(pos2.values()), list(pos3.values()))

    assert len(pos1) == H.num_nodes


def test_pairwise_spring_layout():

    H = xgi.random_hypergraph(10, [0.2], seed=1)

    # seed
    pos1 = xgi.pairwise_spring_layout(H, seed=1)
    pos2 = xgi.pairwise_spring_layout(H, seed=2)
    pos3 = xgi.pairwise_spring_layout(H, seed=2)
    assert pos1.keys() == pos2.keys()
    assert pos2.keys() == pos3.keys()
    assert not np.allclose(list(pos1.values()), list(pos2.values()))
    assert np.allclose(list(pos2.values()), list(pos3.values()))

    assert len(pos1) == H.num_nodes


def test_barycenter_spring_layout():

    H = xgi.random_hypergraph(10, [0.2], seed=1)

    # seed
    pos1 = xgi.barycenter_spring_layout(H, seed=1)
    pos2 = xgi.barycenter_spring_layout(H, seed=2)
    pos3 = xgi.barycenter_spring_layout(H, seed=2)
    assert pos1.keys() == pos2.keys()
    assert pos2.keys() == pos3.keys()
    assert not np.allclose(list(pos1.values()), list(pos2.values()))
    assert np.allclose(list(pos2.values()), list(pos3.values()))

    assert len(pos1) == H.num_nodes

    # phantom
    pos4, G = xgi.barycenter_spring_layout(H, return_phantom_graph=True, seed=1)
    pos5 = xgi.barycenter_spring_layout(H, return_phantom_graph=False, seed=1)
    assert pos4.keys() == pos5.keys()
    assert np.allclose(list(pos4.values()), list(pos5.values()))


def test_weighted_barycenter_spring_layout():

    H = xgi.random_hypergraph(10, [0.2], seed=1)

    # seed
    pos1 = xgi.weighted_barycenter_spring_layout(H, seed=1)
    pos2 = xgi.weighted_barycenter_spring_layout(H, seed=2)
    pos3 = xgi.weighted_barycenter_spring_layout(H, seed=2)
    assert pos1.keys() == pos2.keys()
    assert pos2.keys() == pos3.keys()
    assert not np.allclose(list(pos1.values()), list(pos2.values()))
    assert np.allclose(list(pos2.values()), list(pos3.values()))

    assert len(pos1) == H.num_nodes

    # phantom
    pos4, G = xgi.weighted_barycenter_spring_layout(
        H, return_phantom_graph=True, seed=1
    )
    pos5 = xgi.weighted_barycenter_spring_layout(H, return_phantom_graph=False, seed=1)
    assert pos4.keys() == pos5.keys()
    assert np.allclose(list(pos4.values()), list(pos5.values()))
