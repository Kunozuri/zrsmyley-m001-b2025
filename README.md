GET 1000 historical candle data
IDENTIFY PULLBACK
IDENTIFY SMCstructure
IDENTIFY ORDERBLOCKS























PULLBACK (candle rates): # WILL return data of every pullbacks including internal.
    
    # INITIATION of arrays and variables
    STRUCTURED array of index point, next direction
    INITIALIZE pointer of current high and low index
    INITIALIZE STATIC trend direction (bullish/neutral/bearish)
    INITIALIZE STATIC trend shift signal (continuation/ to be continued)
    
    # IDENTIFY the trend
    IF trend direction is neutral:
        IF current candle high higher than previous candle high:
            SET trend direction to bullish
        ELSE:
            SET it to bearish
    
    # POPULATE array if its first run
    IF structured array is empty:
        IF trend direction is bullish:
            APPEND current index to the structured array and next direction
        ELSE:
            APPEND current index to the structured array and next direction
    
    # CHECK every single candle from last to current
    FOR every index of candle rates starts at 999:
        
        # IGNORE if the candle is correction or protected
        CHECK IF current candle high and low is higher than previous candle || current candle high and low lower than previous candle:
            CONTINUE
        
        # CONTINUATION of bullish
        IF current candle high, higher than previous and candle prev higher than prev-prev:
            SET new high similar to current candle
            SET trend to bullish
            SET trend shift to continuation
        
        # CONTINUATION of bearish
        IF current candle low lower than previous and candle prev lower than prev-prev:
            SET new low similar to current candle
            SET trend to bearish
            SET trend shift to continuation
        
        # TREND shift of bullish
        IF current candle low, lower than previous and candle prev low, higher than prev-prev:
            SET new low similar to current candle
            SET trend to bearish
            SET trend shift to, to be continued
       
        # TREND shift of bearish
        IF current candle high, higher than previous and candle prev high, lower than prev-prev:
            SET new high similar to current candle
            SET trend to bullish 
            SET trend shift to, to be continued
       
        # ADD index point to structured array
        IF trend shift is to be continued:
            IF trend direction to bullish:
                APPEND previous high and next direction to structured array
            ELSE: 
                APPEND previous low and next direction to structured array
       
    RETURN structured arrays



SMCstructure (schematic data): # WILL structure data according to SMC structure.
    
    # INITIALIZATION of arrays and variables
    INITIALIZE STRUCTURED structure record (low index, high index, inducement index, direction)
    INITIALIZE STATIC trend direction (bullish, nuetral, bearish)
    INITIALIZE pointer of high, low, Inducement
    INITIALIZE pointer of previous high, low, inducement
    INITIALIZE STATIC structure record counter
   
    # CHECK every single data in the schematic data
    FOR every point in the schematic data:
        
        # IDENTIFY the trend
        IF trend direction is neutral:
            IF current point is greater than previous:
                SET trend direction to bullish
            ELSE:
                SET trend direction to bearish
        
        # ASSIGNMENT of low, high, inducement variable. aswell as first BOOT of the program
        IF low or high  or inducement is empty:
            
            # FIRST pointer populate
            IF schematic data first index next direction is bullish and current point is equal to schematic data first index:
                SET it as previous low and low pointer
                CONTINUE
            ELSE:
                SET it as previous high and high pointer
                CONTINUE
        
            # SECOND pointer populate
            IF previous high and high is empty:
                SET current point as previous high and high
                CONTINUE
            ELSE:
                SET it as previous low and low
                CONTINUE
            
            # THIRD pointer populate
            IF inducement is empty:
                SET current point as inducement
            
        # CHECK if inducement dont instantly took bos or choch at first boot
        IF high and previous high is the same or low and previous low is the same and current point is lower than inducement and previous low or previous high:
            SET high and low to empty
            SET previous high and low to empty
            SET inducement to empty
            
            CONTINUE
        
        # TRAVERS uptrend structure
        IF trend direction is bullish:
            
            #CHECK the current structure record, if its not empty means it already took inducement.
            IF structure record not empty:
                
                # IDENTIFY if its change of character, and change the direction
                IF trend direction is bullish and current pointer is lower than current structure record index low:
                    SET trend direction to bearish
                    # NOTE: if the trend don't change then its a break of structure
                    
                ADD space to structure record
                INCREMENT structure record counter
                CONTINUE
            
            # IGNORE invalid point but set it as potential inducement marked as low, well be adjusted later.
            IF current point is lower than high pointer and higher than inducement:
                
                # SET low if its the first boot of the program
                IF low is lower than inducement and low is not the same as previous low:
                    SET current point as low
                    CONTINUE
                    
                # SET the low to lower preventing internal structures
                IF current point not higher than low:
                    SET current point as low
                    
                CONTINUE
                
            # IF schematic point formed higher high and adjust the inducement we talk about, if there is. 
            IF current point is higher than high:
                SET high as previous high
                SET current point as high
                
                IF low is higher than inducement:
                    SET low as inducement
                 
                CONTINUE
            
            # APPEND SMCstructure low as CHOCH, high as BOS
            IF current point is lower than inducement and higher than previous low:
                APPEND inducement to structure record
                APPEND high to structure record
                APPEND lower low to structure record
                APPEND direction to structure record
       
       
       # TRAVERS downtrend structure
        IF trend direction is bearish:
            
            #CHECK the current structure record, if its not empty means it already took inducement.
            IF structure record not empty:
                
                # IDENTIFY if its change of character, and change the direction
                IF trend direction is bearish and current pointer is lower than current structure record index high:
                    SET trend direction to bullish
                    # NOTE: if the trend don't change then its a break of structure
                    
                ADD space to structure record
                INCREMENT structure record counter
                CONTINUE
            
            # IGNORE invalid point but set it as potential inducement marked as high, well be adjusted later.
            IF current point is higher than low pointer and lower than inducement:
                
                # SET low if its the first boot of the program
                IF high is higher than inducement and high is not the same as previous high:
                    SET current point as high
                    CONTINUE
                    
                # SET the low to lower preventing internal structures
                IF current point not lower than high:
                    SET current point as high
                    
                CONTINUE
                
            # IF schematic point formed lower low and adjust the inducement we talk about, if there is. 
            IF current point is lower than low:
                SET low as previous low
                SET current point as low
                
                IF high is lower than inducement:
                    SET high as inducement
                 
                CONTINUE
            
            # APPEND SMCstructure low as CHOCH, high as BOS
            IF current point is higher than inducement and lower than previous high:
                APPEND inducement to structure record
                APPEND low to structure record
                APPEND higher high to structure record
                APPEND direction to structure record
    
    RETURN structure record



ORDERBLOCKS (structure record): # RETURN the valid orderblock within the current set of structure (bos, choch, inducement)
    INITIALIZE orderblock storage array
    INITIALIZE available pullback array
    # LOOP each within the structure record
    FOR length of the structure record:
        
        # THIS will hold the pullbacks of every structure from bos to choch
        INITIALIZE temporary schematic data structure array
        
        # IDENTIFY the direction of the current set
        IF current structure record direction is bullish:
            STORE PULLBACK(current structure data low until inducement) TO temporary schematic data 

            # LOOP data to organize proper pullback
            FOR length of the temporary schematic data:
                
                
            
            
        # IDENTIFY the direction of the current set
        IF current structure record direction is bullish: 
