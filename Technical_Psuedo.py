# RETURN the orderblock of the current structure
Technical_Analysis(SMCstructure, interval): #NOTE : interval is the collection of candles
    
    # IDENTIFY orderblocks of the current interval
    ORDERBLOCKS (SMCstructure)
    
    # GET current direction
    GET trend direction from SMCstructure
    
    # CHECK IF current trend is bullish
    IF current trend direction is bullish:
        
        # CHECK IF decisional orderblock is populated and the current price is not below the last decisional orderblock 
        IF ORDERBLOCKS decisional length is not 0 and current price is not below than last decisional:
            
            # LOOP through all the decisional orderblocks
            FOR decisional in the decisionals:
                # IF the current price tapped the decisional high
                IF current price is equal to ORDERBLOCKS decisional candle high:
                    RETURN decisional index and trend direction and "decisional"
        
        # CHECK if it mitigated the engineered liquidity
        IF SMCstructure engineered liquidity is not empty:
            IF current interval candle reference low is lower than engineered liquidity low and current interval candle close is above than engineered liquidity low:
                RETURN engineered liquidity index and trend direction and "engineered liquidity"
        
        # IF the current price tapped the extreme high orderblock 
        IF current price is equal to ORDERBLOCKS extreme candle high:
            RETURN Orderblock index and trend direction and "extreme"
        
        RETURN trend direction
        
    
    # CHECK IF current trend is bullish
    IF current trend direction is bearish:
        
        # CHECK IF decisional orderblock is populated and the current price is not below the last decisional orderblock 
        IF ORDERBLOCKS decisional length is not 0 and current price is not above than last decisional:
            
            # LOOP through all the decisional orderblocks
            FOR decisional in the decisionals:
                # IF the current price tapped the decisional high
                IF current price is equal to ORDERBLOCKS decisional candle low:
                    RETURN decisional index and trend direction and "decisional""
        
        # CHECK if it mitigated the engineered liquidity
        IF SMCstructure engineered liquidity is not empty:
            IF current interval candle reference high is greater than engineered liquidity high and current interval candle close is lower than engineered liquidity high:
                RETURN engineered liquidity index and trend direction and "engineered liquidity"
        
        # IF the current price tapped the extreme high orderblock 
        IF current price is equal to ORDERBLOCKS extreme candle low:
            RETURN Orderblock index and trend direction and "extreme"
        
        RETURN trend direction