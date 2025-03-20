# RETURN the list of SNR
SUPPORT_RESISTANT (SMCstructure):
    
    # INITIALIZE structure that will hold the data of current high and low and identify if its support or resistance
    INITIALIZE support_resistance structure {
        upper,
        lower,
        label
    }
    
    # INITIALIZE reference point of the current candlestick
    INITIALIZE upper reference point
    INITIALIZE lower reference point
    INITIALIZE previous direction
    
    INITIALIZE range
    
    # LOOP entire SMCstructure
    FOR every current point in the SMCstructure:
        
        # CHECK the upper and lower if they are empty
        IF upper reference or lower reference is empty:
            
            # CHECK IF the current direction is bullish and the last direction is not yet set
            IF  previous direction is empty:
                SET previous direction as current point direction 
                
                # IDENTIFY direction to choose where to populate first
                IF current point direction is bullish:
                    SET lower reference point as current point last pullback
                ELSE:
                    SET upper reference point as current point last pullback
                
                CONTINUE
            
            # CHECK IF we have the same set of direction to the previous
            IF previous direction is equal to current point direction:
                SET lower and upper reference point and previous direction to empy
                CONTINUE
            
            # IDENTIFY direction to populate the remaining empty reference
            IF upper reference is empty and previous direction is bullish:
                SET upper reference as current point high
                CONTINUE
            
            # ELSE set it to the other side
            SET lower reference as current point low
            CONTINUE
            
        # CALCULATE the 80% from lower to upper if the direction is bullish
        IF previous direction is bullish:
            SET range as upper reference - lower reference
            SET range as range * .80
            SET range as lower reference + range
            SET lower reference as range
        
        # ELSE its bearish and get the 20% from lower to high
        ELSE:
            SET range as upper reference - lower reference
            SET range as range * .20
            SET range as upper reference + range
            SET upper reference as range
        
        # APPEND the information of the SNR and set its label
        SET upper and lower reference as support_resistance structure upper and lower
        
        IF previous direction is bullish:
            SET support_resistance label as "resistance"
        
        ELSE:
            SET support_resistance label as "support"
            
        INCREMENTS support_resistance structure size
        SET upper and lower reference point and  previous direction and range to empty
    
    RETURN support_resistance structure