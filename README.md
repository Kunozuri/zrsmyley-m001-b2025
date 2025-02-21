# zrsmyley-m001-b2025
This something you dont know.


GET 1000 historical candle data
IDENTIFY PULLBACK()
IDENTIFY SMCstructure ()
























PULLBACK (candle rates):
    STRUCTURED array of index point, next direction
    INITIALIZE pointer of current high and low index
    INITIALIZE STATIC trend direction (bullish/neutral/bearish)
    INITIALIZE STATIC trend shift signal (continuation/ to be continued)
    
    IF trend direction is neutral:
        IF current candle high higher than previous candle high:
            SET trend direction to bullish
        ELSE:
            SET it to bearish
    
    FOR every index of candle rates starts at 999:
        
        # IGNORE if the candle is correction or protected
        CHECK IF current candle high and low is higher than previous candle || current candle high and low lower than previous candle:
            CONTINUE
        
        # POPULATE array if its first run
        IF structured array is empty:
            IF trend direction is bullish:
                APPEND current index to the structured array and next direction
            ELSE:
                APPEND current index to the structured array and next direction
        
        # bullish continuation
        IF current candle high, higher than previous and candle prev higher than prev-prev:
            SET new high similar to current candle
            SET trend to bullish
            SET trend shift to continuation
        
        # bearish continuation
        IF current candle low lower than previous and candle prev lower than prev-prev:
            SET new low similar to current candle
            SET trend to bearish
            SET trend shift to continuation
        
        # bullish trend shift
        IF current candle low, lower than previous and candle prev low, higher than prev-prev:
            SET new low similar to current candle
            SET trend to bearish
            SET trend shift to, to be continued
       
       # bearish trend shift
       IF current candle high, higher than previous and candle prev high, lower than prev-prev:
            SET new high similar to current candle
            SET trend to bullish 
            SET trend shift to, to be continued
       
       # add index point to structured array
       IF trend shift is to be continued:
            IF trend direction to bullish:
                APPEND previous high and next direction to structured array
            ELSE: 
                APPEND previous low and next direction to structured array
       
       RETURN structured arrays




SMCstructure (schematic data):
    
    # INITIALIZATION of arrays and variables
    INITIALIZE STRUCTURED structure record (low index, high index, inducement index, direction)
    INITIALIZE STATIC trend direction (bullish, nuetral, bearish)
    INITIALIZE pointer of high, low, Inducement
    INITIALIZE pointer of previous high, low, inducement
    INITIALIZE STATIC structure record counter
    
    # IDENTIFY the trend
    FOR every point in the schematic data:
        IF trend direction is neutral:
            IF current point is greater than previous:
                SET trend direction to bullish
            ELSE:
                SET trend direction to bearish
        
        # ASSIGNMENT of low, high, inducement variable. aswell as first BOOT of the program
        IF low or high  or inducement is empty:
            
            # FIRST pointer populate
            IF schematic data first index next direction is bullish and current point is equal to schematic data first index:
                SET it as low pointer
                CONTINUE
            ELSE:
                SET it as high pointer
                CONTINUE
        
            # SECOND pointer populate
            IF high is empty:
                SET current pointer as high and previous high 
                CONTINUE
            ELSE:
                SET it as low and previous low
                CONTINUE
            
            # THIRD pointer populate
            IF Inducement is empty:
                SET current pointer as inducement
                CONTINUE
        
        # TRAVERS uptrend structure
        IF trend direction is bullish:
            
            #CHECK the current structure record, if its not empty means it already took inducement.
            IF structure record index counter not empty:
                
                # IDENTIFY if its break of structure
                IF current pointer is higher than current structure record index high: 
                    ADD space to structure record
                    INCREMENT structure record counter
                    CONTINUE
               
                # IDENTIFY if its change of character, and change the direction
                ELSE IF current pointer is lower than current structure record index low:
                    ADD space to structure record
                    INCREMENT structure record counter
                    SET trend direction to bearish
                    CONTINUE
            
            # IGNORE invalid point but set it as potential inducement marked as low, well be adjusted later.
            IF current point is lower than high pointer and higher than inducement:
                
                # SET the low to lower preventing internal structures
                IF current pointer not higher than low:
                    SET current pointer as low
                    
                CONTINUE
                
            # IF schematic point formed higher high and adjust the inducement we talk about, if there is. 
            IF current point is higher than high pointer:
                SET high as previous high
                SET current point as high
                
                IF low is higher than inducement:
                    SET low as inducement
                 
                CONTINUE
            
#            # [PS: I HAVE NO IDEA WHY I MADE THIS] CHECK if there's a new low for Inducement refinance
#            IF current point is not lower than low and inducement but higher than previous low:
#                SET inducement as the current point
#                CONTINUE
            
            # APPEND SMCstructure low as CHOCH, high as BOS
            IF current point is lower than inducement and low and higher than previous low:
                APPEND inducement to SMCstructure as inducement
                APPEND high to SMCstructure as high
                APPEND lower low to SMCstructure as low
                
                
                    
                    
            IF 
        
        # TRAVERS downtrend structure
        IF current point lower than high pointer:
            SET current pointer as low
        
        # MARK possible inducement
        
        
            
