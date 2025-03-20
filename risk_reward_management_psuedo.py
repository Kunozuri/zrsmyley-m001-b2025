# RETURNS the price of the stoploss
STOPLOSS (SMCstructure, orderblock index, trading style, entry price, is_trailing):
    
    # INITIALIZE the holder of ATR to get the stoploss
    
    # INITIALIZE Multiplier depending on the interval
    SWITCH trading style:
        CASE scalping:
            INITIALIZE multiplier to 1
            
        CASE intra-day:
            INITIALIZE multiplier to 2
            
        CASE swing:
            INITIALIZE multiplier to 3
        
        CASE positional:
            INITIALIZE multiplier to 4
     
       # IDENTIFY the direction of the trend
       IF SMCstructure trend direction is bullish:
           
           INITIALIZE ATR stoploss as entry price - ATR * Multiplier
           INITIALIZE SMCstructure stoploss as orderblock index
           
           # CHECK IF this is a trail stop
           IF is_trailing:
               RETURN ATR stoploss
       
           IF ATR stoploss is lower than SMCstructure:
               RETURN ATR stoploss
               
           ELSE:
               RETURN SMCstructure stoploss
       
       # IDENTIFY the direction of the trend
       IF SMCstructure trend direction is  bearish:
       
           INITIALIZE ATR stoploss as entry price + ATR * Multiplier
           INITIALIZE SMCstructure stoploss as orderblock index
           
           # CHECK IF this is a trail stop
           IF is_trailing:
               RETURN ATR stoploss
               
           IF ATR stoploss is higher than SMCstructure:
               RETURN ATR stoploss
               
           ELSE:
               RETURN SMCstructure stoploss
           
        
# RETURN the price to take the profit
TAKE PROFIT (SMCstructure, RSI):
    
    # IDENTIFY trend direction
    IF SMCstructure trend direction is bullish:

        # CHECK IF the current price is equal or above the SMCstructure
        IF current price is above or equal SMCstructure index high:
            RETURN current price
    
    # IDENTIFY trend direction
    IF SMCstructure trend direction is bearish:

        # CHECK IF the current price is equal or below the SMCstructure
        IF current price is below or equal SMCstructure index low:
            RETURN current price
    
    RETURN NONE



TRADE EXECUTION (symbol, ordertype, lotsize, stoploss, takeprofit):
    