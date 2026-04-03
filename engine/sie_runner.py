"""
SIE Runner — executes all layers in sequence for a given property.
"""
from engine.layers import (
    layer_0_ape, layer_1_signals, layer_1a_tdlr,
    layer_2_freshness, layer_3_spi, layer_4_structure,
    layer_5_yield, layer_6_ycs, layer_7_bid,
    layer_8_competition, layer_9_strategy,
    layer_10_recommendation, layer_11_outcome
)


def run_sie(property_data: dict) -> dict:
    """
    Run all SIE layers in order. Returns full analysis dict.
    """
    result = {}

    result["L0_APE"]             = layer_0_ape.run(property_data)
    result["L1_Signals"]         = layer_1_signals.run(property_data)
    result["L1A_TDLR"]           = layer_1a_tdlr.run(property_data)
    result["L2_Freshness"]       = layer_2_freshness.run(property_data)
    result["L3_SPI"]             = layer_3_spi.run(property_data)
    result["L4_Structure"]       = layer_4_structure.run(property_data)
    result["L5_Yield"]           = layer_5_yield.run(property_data)
    result["L6_YCS"]             = layer_6_ycs.run(property_data)
    result["L7_Bid"]             = layer_7_bid.run(property_data)
    result["L8_Competition"]     = layer_8_competition.run(property_data)
    result["L9_Strategy"]        = layer_9_strategy.run(property_data)
    result["L10_Recommendation"] = layer_10_recommendation.run(property_data)
    result["L11_Outcome"]        = layer_11_outcome.run(property_data)

    return result
