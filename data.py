from metrics import psi_value, hellinger_value

from numpy import array
from scipy.stats import skewnorm
from random import random


def generate_base_parameters():

    a = random() * 5
    loc = 0
    scale = 1 + (random() - 0.5)

    return dict(
        a=a,
        loc=loc,
        scale=scale
    )


def update_parameters(a, loc, scale):

    a += (random() - 0.5) * a * 0.5
    loc += (random() - 0.5) * loc * 0.5
    scale += (random() - 0.5) * scale * 0.5

    return dict(
        a=a,
        loc=loc,
        scale=scale
    )


def generate_distributions(num_samples):
    params = generate_base_parameters()
    alternate_params = update_parameters(**params)

    main_data = generate_data(num_samples, **params)
    alternate_data = generate_data(num_samples, **alternate_params)

    psi, hellinger = generate_metrics(main_data, alternate_data)

    return main_data, alternate_data, psi, hellinger


def generate_data(num_samples, a, loc, scale):

    data = []
    for _ in range(num_samples):
        data.append(skewnorm.rvs(a, loc, scale))

    return array(data)


def generate_metrics(main_data, alternate_data):
    psi = psi_value(main_data, alternate_data),
    hellinger = hellinger_value(main_data, alternate_data)

    return psi, hellinger
