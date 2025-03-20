# ENTRY that will be run in low interval such as M1-M15
Single Mitigation Entry(orderblock, Interval, direction):
    
    # INITIALIZE current reference start at 2nd candle
    INITIALIZE current reference point
    INITIALIZE candle rates
    
    # RANGE of the orderblock confirmation limits
    INITIALIZE range : subtract high and low of orderblock
    
    # IDENTIFY which trend is currently majority
    IF direction is bullish:
        
        INITIALIZE low limit : orderblock low - range
        INITIALIZE high limit : orderblock high + (range x 2)
        
        # CHECK IF every candle is not out of the range to look for entry confirmation
        IF current reference point - 1 close is not less than low limit  and not above high limit:
        
            INITIALIZE inefficiency : current candle reference point subract its high and low then divide 2
            
            # IDENTIFY if a candle ready for mitigation
            IF close of current reference point is higher than open of current reference point + 1 and close of current reference point - 1 is higher than inefficiency:
                RETURN high of current reference point
            
    # IDENTIFY which trend is currently majority
    IF direction is bearish:
          
        INITIALIZE low limit : orderblock low - (range x 2)
        INITIALIZE high limit : orderblock high + range
          
        # CHECK IF every candles is not out of the range to look for entry confirmation
        IF current reference point - 1 close is not greater than high limit and not below low limit:
            
            INITIALIZE inefficiency : current candle reference point subract its high and low then divide 2
            
            # IDENTIFY if a candle ready for mitigation
            IF close of current reference point is lower than open of current reference point + 1 and close of current reference point - 1 is lower than inefficiency:
                RETURN high of current reference point
            

# ENTRY for low interval change of character with and without inducement filtered
Choch Entry (orderblock, entry interval, direction):
    
    # INITIALIZE current reference start at 2nd candle
    INITIALIZE current reference point as interval first index

    INITIALIZE orderblocks (SMCstructure, entry interval)
    
    # IDENTIFY trend direction 
    IF direction is bullish:
        
        # if it tapped the current orderblock then start looking for single candle confirmation
        IF current reference point is below or equal to orderblock extreme high:
            Single Mitigation Entry(orderblock, entry interval, direction)
            RETURN single candle mitigation price
    
    # IDENTIFY trend direction 
    IF direction is bearish:
        
        # if it tapped the current orderblock then start looking for single candle confirmation
        IF current reference point is above or equal to orderblock extreme low:
            Single Mitigation Entry(orderblock, entry interval, direction)
            RETURN single candle mitigation price
    
