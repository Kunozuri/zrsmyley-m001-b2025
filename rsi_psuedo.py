# RETURN the extreme entry point of SMCstructure
RSI (SMCstructure):
    
    # GET the 1000 RSI data
    INITIALIZE RSI holder
    
    #INITIALIZE two point holder for impulse and pullback control
    INITIALIZE penultimate point
    INITIALIZE previous point
    
    # IDENTIFY the current direction of the SMCstructure
    IF SMCstructure trend direction is bullish:
    
        SET penultimate point to SMCstructure low
        SET previous point to SMCstructure high
        
        IF current RSI holder is equal to RSI holder index penultimate point:
            RETURN TRUE
        
        ELSE:
            RETURN FALSE
    
    
    # IDENTIFY the current direction of the SMCstructure
    IF SMCstructure trend direction is bearish:
        
        SET penultimate point to SMCstructure high
        SET previous point to SMCstructure low
        
        IF current RSI holder is equal to RSI holder index penultimate point:
            RETURN TRUE
        
        ELSE:
            RETURN FALSE