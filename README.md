GET 1000 historical candle data
IDENTIFY SCHEMATIC
IDENTIFY SMCstructure
IDENTIFY ORDERBLOCKS























SCHEMATIC (candle rates): # WILL return data of every schematic including internal.
    
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
    INITIALIZE STRUCTURED structure record (low index, high index, inducement index, pullback record, direction)
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
                IF current point close is lower than current structure record index low:
                    SET trend direction to bearish
                    ADD space to structure record
                    INCREMENT structure record counter
                    CONTINUE
                
                # REFINE the choch point if invalid closure
                ELSE IF current point close is higher than current structure record index low and current point low is lower than current structure record index low:
                    SET current structure record low as current point
                    CONTINUE
                
                # REFINE the bos point if invalid closure
                IF current point close lower than high and current point high is higher than high:
                    SET current structure record high as current point
                    CONTINUE
                
                # IF the trend don't change then its a break of structure
                IF current point close higer than high:
                    ADD space to structure record
                    INCREMENT structure record counter
                    CONTINUE
                
                # IGNORE every point if none of the condition above is met
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
                    APPEND inducement to pullback record
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
                
                IF structure record not empty:
                
                # IDENTIFY if its change of character, and change the direction
                IF current point close is higher than current structure record index high:
                    SET trend direction to bullish
                    ADD space to structure record
                    INCREMENT structure record counter
                    CONTINUE
                
                # REFINE the choch point if invalid closure
                ELSE IF current point close is lower than current structure record index high and current point high is higher than current structure record index high:
                    SET current structure record high as current point
                    CONTINUE
                
                # REFINE the bos point if invalid closure
                IF current point close higher than high and current point low is lower than low:
                    SET current structure record low as current point
                    CONTINUE
                
                # IF the trend don't change then its a break of structure
                IF current point close lower than low:
                    ADD space to structure record
                    INCREMENT structure record counter
                    CONTINUE
                
                # IGNORE every point if none of the condition above is met
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
                    APPEND inducement to pullback record
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
    INITIALIZE struct orderblock storage array (extreme, decisional, liquidities)
    
    # LOOP each within the structure record
    FOR the length of the structure record:
        INITIALIZE current point holder # holder of the current candle, such as the extreme point
    
        # IDENTIFY the direction of the current set
        IF current structure record direction is bullish:
            
            # LOOP while untill I break it
            WHILE TRUE:
                
                INITIALIZE current point holder # HOLDER of the extreme and decisional point
                INITIALIZE next of current point holder
                INITIALIZE next next of current point holder
                
                #CHECK if the current point has a hieght of 60 pips also known as point of interest
                IF current point holder ((high - low) / _Digit) is greater than 60pips:
                    
                    # EXIT if it has already extreme orderblock
                    IF orderblock storage array extreme is not empty and current point holder is below structure record pullback:
                        SET current point holder to structure record pullback index 1
                        CONTINUE
                    
                    # CHECK if the current point close is above 75% of the whole candle
                    IF current point holder close is above ((high - low) * 0.75):
                        
                        # CHECK if the next low is not less than 55% of the whole candle
                        IF next point holder low is above current point holder ((high - low) * 0.6):
                            APPEND current point holder to orderblock storage array extreme
                        
                        # CHECK if it has eniffeciency in the middle
                        ELSE IF next current holder close is above current point holder (((high - low) // 2) * 3) and next next current point holder low is 20% higher than next current point holder open:
                            APPEND current point holder to orderblock storage array extreme
                        
                        IF orderblock storage array is empty:
                            SET current point holder to next current point
                            CONTINUE
                        
                        SET current point holder to structure record pullback index 1
                        CONTINUE
                
                #
                ELSE IF
                            
            
            
            
            
            
