# RETURN structure data according to SMC structure.
SMCstructure (schematic data, interval):
       
    # INITIALIZATION of arrays and variables
    INITIALIZE STRUCTURED structure record (
        high reference,
        low reference,
        inducement reference,
        array of pullback record [] pullback references,
        structure direction,
        interval )
        
    INITIALIZE STATIC trend direction (bullish, nuetral, bearish)
    INITIALIZE STATIC structure record counter
    INITIALIZE references of high, low, Inducement
    INITIALIZE references of higher high, lower low
    
    # CHECK every single data in the schematic data
    FOR every references in the schematic data:
        
        # IDENTIFY the trend and SETUP first run of the program
        IF trend direction is neutral:
            
            # POPULATE first reference
            IF schematic data first reference point is greater than second reference point and low reference and high is empty:
                SET current reference as lower low and low reference
                CONTINUE
                
            ELSE:
                SET current reference as higer high and high reference
                CONTINUE
            
            # POPULATE second reference
            IF higher high and high is empty:
               SET current reference as higher high and high reference
               CONTINUE
           
           ELSE:
               SET current reference as lower low and low reference
               CONTINUE
           
           # POPULATE inducement reference
           IF inducement is empty:
               SET current reference as inducement
               CONTINUE
           
           # SET smart money concept trend direction
            IF schematic data first reference point is greater than second reference point:
                SET trend direction to bullish
                
            ELSE:
                SET trend direction to bearish
           
            # CHECK IF inducement dont instantly took bos or choch
            IF current reference point is lower than inducement and lower low and trend direction is bullish:
                SET high and low to empty
                SET higher high and lower low to empty
                SET inducement to empty
                SET trend direction to neutral
                CONTINUE
                
            IF current reference point is higher than inducement and higher high and trend direction is bearish:
                SET high and low to empty
                SET higher high and lower low to empty
                SET inducement to empty
                SET trend direction to neutral
                CONTINUE
                
            CONTINUE

        
        # TRAVERS uptrend structure
        IF trend direction is bullish:
            
            #CHECK the current structure record, if its not empty means it already took inducement.
            IF structure record not empty:
                
                # IDENTIFY if its in the lower interval change of character
                IF interval is less than 5 and current reference point high is higher than inducement:
                    RETURN structure record first references
                
                # IDENTIFY if its change of character, and change the direction
                ELSE IF current reference point close is lower than current structure record reference low:
                    SET trend direction to bearish
                    INCREMENT structure record space
                    INCREMENT structure record counter
                    CONTINUE
               
               # IF the trend don't change then its a break of structure
                IF current reference point close higher than current structure record reference high:
                    INCREMENT structure record space
                    INCREMENT structure record counter
                    CONTINUE
                 
                # REFINE the choch point if invalid closure
                ELSE IF current reference point close is higher than current structure record reference low and low of current reference point is lower than current structure record reference low:
                    SET current reference point as current structure record reference low
                    CONTINUE
                
                # REFINE the bos point if invalid closure
                IF current reference point close lower than current structure reference high and current reference point high is higher than current structure record reference high:
                    SET current reference point as current structure record reference high
                    CONTINUE
                
                # IGNORE every point if none of the condition above is met
                CONTINUE
            
            # HANDLE fake change of character
            IF current structure record reference inducement is empty and current reference point close is lower than current structure counter - 1 reference low:
                SET structure record counter - 1 trend direction to bearish
                SET structure record counter - 1 low as current reference point
                SET structure record counter - 1 high as schematic data previous reference
                SET trend direction to bearish
                CONTINUE
            
            # IGNORE invalid point but set it as potential inducement marked as low, well be adjusted later.
            IF current reference point high is lower than higher high and higher than inducement:
                
                # SET low if its the first boot of the program
                IF low is lower than inducement and low is equal to lower low:
                    SET low as current reference point
                    CONTINUE
                    
                # SET the low to even lower preventing internal structures
                IF current reference point is lower than low:
                    SET low as current reference point
                    
                CONTINUE
                
            # IF schematic point formed higher high and adjust the inducement we talk about, if there is. 
            IF current reference point is higher than higher high:
                SET higher high as high
                SET current point as higher high
                
                IF low is higher than inducement:
                    APPEND inducement to pullback record
                    SET low as inducement 
                
                CONTINUE
            
            # APPEND SMCstructure low as CHOCH, high as BOS
            IF current reference point is lower than inducement:
                APPEND inducement to structure record
                APPEND higher high to structure record
                APPEND lower low to structure record
                APPEND trend direction to structure record
       
      
       # TRAVERS downtrend structure
        IF trend direction is bearish:
            
            # CHECK the current structure record, if its not empty means it already took inducement.
            IF structure record not empty:
                
                # IDENTIFY if its in the lower interval change of character
                IF interval is less than 5 and current reference point low is lower than inducement:
                    RETURN structure record first references
                    
                # IDENTIFY if its change of character, and change the direction
                ELSE IF current reference point close is higher than current structure record reference high:
                    SET trend direction to bullish
                    INCREMENT structure record space
                    INCREMENT structure record counter
                    CONTINUE
                
                # IF the trend don't change then its a break of structure
                IF current reference point close is lower than current structure record reference low:
                    INCREMENT structure record space
                    INCREMENT structure record counter
                    CONTINUE
                
                # REFINE the choch point if invalid closure
                ELSE IF current reference point close is lower than current structure record reference high and high of current reference point is higher than current structure record reference high:
                    SET current reference point as current structure record reference high
                    CONTINUE
                
                # REFINE the bos point if invalid closure
                IF current reference point close higher than current structure reference low and current reference point low is lower than current structure record reference low:
                    SET current reference point as current structure record reference low
                    CONTINUE
                
                # IGNORE every point if none of the condition above is met
                CONTINUE
            
            # HANDLE fake change of character
            IF current structure record reference inducement is empty and current reference point close is higher than current structure counter - 1 reference high:
                SET structure record counter - 1 trend direction to bullish
                SET structure record counter - 1 high as current reference point
                SET structure record counter - 1 low as schematic data previous reference
                SET trend direction to bullish 
                CONTINUE
                
            # IGNORE invalid point but set it as potential inducement marked as low, well be adjusted later.
            IF current reference point low is higher than lower low and lower than inducement:
                
                # SET high if its the first boot of the program
                IF high is higher than inducement and high is equal to higher high:
                    SET high as current reference point
                    CONTINUE
                    
                # SET the high to even higher preventing internal structures
                IF current reference point is higher than high:
                    SET high as current reference point
                    
                CONTINUE
                
            # IF schematic point formed lower low and adjust the inducement we talk about, if there is. 
            IF current reference point is lower than lower low:
                SET lower low as low
                SET current point as lower low
                
                IF high is lower than inducement:
                    APPEND inducement to pullback record
                    SET high as inducement 
                
                CONTINUE
            
            # APPEND SMCstructure low as CHOCH, high as BOS
            IF current reference point is lower than inducement:
                APPEND inducement to structure record
                APPEND higher high to structure record
                APPEND lower low to structure record
                APPEND trend direction to structure record
       
    RETURN structure record first references