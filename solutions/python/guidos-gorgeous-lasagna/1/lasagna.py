"""Functions used in preparing Guido's gorgeous lasagna."""

EXPECTED_BAKE_TIME = 40  # Tempo total de forno (minutos)
PREPARATION_TIME = 2     # Tempo por camada (minutos)

def bake_time_remaining(elapsed_bake_time):
    """Return remaining bake time (in minutes)."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(num_layers):
    """Calculate preparation time based on layers."""
    return num_layers * PREPARATION_TIME

def elapsed_time_in_minutes(num_layers, elapsed_bake_time):
    """Return total elapsed time (prep + bake)."""
    return preparation_time_in_minutes(num_layers) + elapsed_bake_time