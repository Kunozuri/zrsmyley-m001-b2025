# RETURN data of every schematic Impulse and Pullback
SCHEMATIC (candle rates):
    
    # INITIALIZATION of arrays and variables
    STRUCTURED array of reference, reference point (index_1/ index_1.low)
    INITIALIZE reference of current candle high and low
    INITIALIZE STATIC trend direction (bullish/neutral/bearish)
    INITIALIZE STATIC trend shift signal (continuation/ to be continued)
    
    # IDENTIFY the trend and POPULATE array on first run
    IF trend direction is neutral:
        IF current candle high is higher than previous candle high:
            SET trend direction to bullish
            APPEND current reference to the structured array and reference point
            
        ELSE:
            SET trend direction to bearish
            APPEND current reference to the structured array and reference point
    
    # TRAVERSE candle starting from second to the last upto current reference
    FOR every reference of candle rates starts at 999 down to 0:
        
        # IGNORE if the candle is protected
        IF current candle high is lower than high of reference high and current candle low is higher than low of reference high:
            CONTINUE
        
        # RECONSIDER if the candle is correction
        IF trend direction is bullish:
            IF current candle low is lower than low of reference high and current candle close is higher than open of reference high and current candle high is higher than high of reference high:
                SET high as current candle
            CONTINUE
            
        ELSE:
            IF current candle high is higher than high of reference low and current candle close is lower than open of reference low and current candle low is lower than low of reference low:
                SET low as current candle
            CONTINUE
        
        # BULLISH continuation
        IF current candle high is lower than high of reference high and high of reference high is higher than high of reference high - 1:
            SET high as current candle
            SET trend shift to continuation
            CONTINUE
        
        # BEARISH continuation
        IF current candle low is higher than low of reference low and low of reference low is lower than low of reference low - 1:
            SET low as current candle
            SET trend shift to continuation
            CONTINUE
        
        # BULLISH trend shift
        IF current candle low is lower than low of reference high and low of reference high is higher than low of reference high - 1:
            SET trend shift to : to be continued
       
        # BEARISH trend shift
        IF current candle high is higher than high of reference low and high of reference low is higher than high of reference low - 1:            SET trend to bullish 
            SET trend shift to : to be continued
       
        # ADD reference and reference point to structured array and SHIFT direction of traversing
        IF trend shift is to be continued:
            IF trend direction to bullish:               
                APPEND high reference and reference point to structured array
                SET low as current candle
                SET trend to bearish
            
            ELSE: 
                APPEND low reference and reference point to structured array
                SET high as current candle
                SET trend to bullish
                
    RETURN structured array