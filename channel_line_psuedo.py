# IDENTIFY a possible trendlines within the current structure
TREND CHANNEL (SMCstructure, interval):
    
    # INITIALIZE storage array that will hold the data of current trendline in the structure
    INITIALIZE channel line structure {
        head,
        body array,
        tail,
        direction
    }
    
    # INITIALIZE reference point of the current candlestick
    INITIALIZE first reference point
    INITIALIZE second reference point
    INITIALIZE previous trend direction
    INITIALIZE next price point
    INITIALIZE trend tap counter to 3
    INITIALIZE line channel counter
    
    # INITIALIZE variables that will be used to determine line point
    INITIALIZE slope price
    INITIALIZE Y intercept
    
    # TRAVERS every structure
    FOR current reference point every SMCstructure:
        
        # POPULATE the references
        IF second reference is empty:
            IF first reference is empty:
                SET current reference last pullback to first reference point
                SET current trend direction as previous trend direction
                CONTINUE
                
            SET current reference first pullback to second reference point
            
            # CHECK IF it changes character to validate the line channel
            IF previous trend direction is not equal to current trend direction:
                
                # SET direction of the line channel
                IF current reference direction is bullish:
                    SET channel line structure direction to bullish
                
                ELSE: 
                    SET channel line structure direction to bearish
                
                SET channel line structure head to first reference point
                CONTINUE
            
            # EMPTYING the references because its invalid trendline
            SET first and second reference point to empty 
            CONTINUE
        
        # IDENTIFY direction of the line channel
        IF current channel line structure direction is bullish:
            
            # SET UP nessesarry price point
            SET slope as (second reference - first reference) / (2 - 1)
            SET Y intercept as first reference - (slope * 1)

            SET next point price as (slope * trend tap counter) + Y intercept
            
            # CHECK IF only tapped the line channel
            IF current reference point low.close is above next point price:
                
                # SET tail if its empty
                IF channel line structure tail is empty:
                    SET current reference point low to channel line structure tail
                    INCREMENT trend tap counter
                    CONTINUE
                
                # APPEND tail to the body and SET the current point to tail
                APPEND channel line structure tail to channel line structure body array
                SET current reference point low to channel line structure tail
                INCREMENT trend tap counter
                CONTINUE
        
        # IDENTIFY direction of the line channel
        IF current channel line structure direction is bearish:
            
            # SET UP nessesarry price point
            SET slope as (first reference - second reference) / (2 - 1)
            SET Y intercept as second reference - (slope * 1)
            
            SET next point price as Y intercept - (slope * trend tap counter)
        
            # CHECK IF only tapped the line channel
            IF current reference point high.close is below next point price:
                
                # SET tail if its empty
                IF channel line structure tail is empty:
                    SET current reference point high to channel line structure tail
                    INCREMENT trend tap counter
                    CONTINUE
                
                # APPEND tail to the body and SET the current point to tail
                APPEND channel line structure tail to channel line structure body array
                SET current reference point high to channel line structure tail
                INCREMENT trend tap counter
                CONTINUE
    
        INCREMENT line channel structure and line channel counter by 1
        SET trend tap counter to 3
    
    # RETURN the whole set of line channel group and the current point to be tapped
    RETURN channel line structure and next point price