# RETURN the valid orderblock within structure (bos, choch, inducement)
ORDERBLOCKS (structure record):
    INITIALIZE struct orderblock storage array (
    extreme,
    decisional,
    engineered liquidity,
    liquidities)
    INITIALIZE static decisional counter
    
    # TRAVERSE every structure set in structure record
    FOR the length of the structure record:
        
        # GET the size of the structure pullback record
        INITIALIZE length of the structure record pullback
                 
        # IDENTIFY the direction of the current set
        IF current structure record direction is bullish:
            
            # HOLDER of the extreme and decisional point
            INITIALIZE current point holder
            
            INITIALIZE next of current point holder
            INITIALIZE next next of current point holder
  
            # LOOP untill I break it
            WHILE TRUE:
                
                # BREAK if it reach inducement
                IF current point holder is equal to structure record inducement:
                    SET decisional counter to 0
                    BREAK
                
                # ASSIGN as liquidities if pullback is not a valid orderblock.
                IF current point holder is equal to structure record pullback index counter and orderblock storage array decisional length is less than to counter - 1:
                    
                    # ASSIGN as engineered liquidity if its the first index
                    IF current point holder is equal to structure record pullback index 1:
                        APPEND current point holder as orderblock storage array engineered liquidity
                    
                    ELSE:
                        APPEND current point holder as orderblock storage array liquidities
                
                # CHECK if the current point close is above 75% of the whole candle and is a long wyck also known as POI
                IF current point holder ((high - low) / _Digit) is greater than 60pips and current point holder close is above ((high - low) * 0.75):
                            
                    # CHECK if the next low is not less than 60% of the whole candle
                    IF next current point holder low is above the current point holder ((high - low) * 0.6) aswell as next next current point holder:
                                       
                        # ORGANIZE where to append
                        IF orderblock storage array extreme is empty and current point holder is lower than structure record pullback index 1:
                            APPEND current point holder to orderblock storage array extreme
                                
                        ELSE IF orderblock storage array decisional is empty and current point holder is equal or above to pullback index 1:
                            APPEND current point holder to orderblock storage array decisional
                            
                    # CHECK if it has eniffeciency
                    ELSE IF next current holder close and next next current point holder low is above current point holder high + (((high - low) // 2) * 3):
                            
                        # ORGANIZE where to append
                        IF orderblock storage array extreme is empty and current point holder is lower than structure record pullback index 1:
                            APPEND current point holder to orderblock storage array extreme
                                
                        ELSE IF orderblock storage array decisional is empty and current point holder is equal or above to pullback index 1:
                            APPEND current point holder to orderblock storage array decisional
                                
                # CHECK if it has eniffeciency if it is only an ordinary order block
                ELSE IF next current holder close and next next current point holder low is above current point holder high + (((high - low) // 2) * 3):
                            
                    # ORGANIZE where to append
                    IF orderblock storage array extreme is empty and current point holder is lower than structure record pullback index 1:
                        APPEND current point holder to orderblock storage array extreme
                                
                    ELSE IF orderblock storage array decisional is empty and current point holder is equal or above to pullback index 1:
                        APPEND current point holder to orderblock storage array decisional
                          
                # IF above condition filled about extreme orderblock
                IF orderblock storage array extreme is not empty and current point holder is less than storage structure pullback index 1:
                    SET current point holder to structure record pullback index 1
                    CONTINUE
                        
                # IF above condition filled about decisional orderblock
                IF orderblock storage array decisional is not empty and current point holder is equal or higher than storage structure pullback index 1:
                            
                    # LOOP until the end of the size
                    IF decisional counter is less than length of structure record pullback + 1:
                        SET current point holder to structure record pullback index counter
                        INCREMENT decisional counter 
                        CONTINUE
                    
                #ADVANCE pointers by one
                SET current point holder to next current point
                SET next current point holder to next next current point
                SET next next current point holder to next next next current point
                CONTINUE
                            
            
        # IDENTIFY the direction of the current set
        IF current structure record direction is bearish:
            
            # HOLDER of the extreme and decisional point
            INITIALIZE current point holder
            
            INITIALIZE next of current point holder
            INITIALIZE next next of current point holder
  
            # LOOP while untill I break it
            WHILE TRUE:
                
                # BREAK if it reach inducement
                IF current point holder is equal to structure record inducement:
                    SET decisional counter to 0
                    BREAK
                
                # ASSIGN as liquidities if pullback is not a valid orderblock.
                IF current point holder is equal to structure record pullback index counter and orderblock storage array decisional length is less than to counter - 1:
                    
                    # ASSIGN as engineered liquidity if its the first index
                    IF current point holder is equal to structure record pullback index 1:
                        APPEND current point holder as orderblock storage array engineered liquidity
                    
                    ELSE:
                        APPEND current point holder as orderblock storage array liquidities
                
                # CHECK if the current point close is below 25% of the whole candle and is a long wyck also known as POI
                IF current point holder ((high - low) / _Digit) is greater than 60pips and current point holder close is below ((high - low) * 0.25):
                            
                    # CHECK if the next high is not greater than 40% of the whole candle
                    IF next current point holder high is below the current point holder ((high - low) * 0.4) aswell as next next current point holder:
                                       
                        # ORGANIZE where to append
                        IF orderblock storage array extreme is empty and current point holder is higher than structure record pullback index 1:
                            APPEND current point holder to orderblock storage array extreme
                                
                        ELSE IF orderblock storage array decisional is empty and current point holder is equal or below to pullback index 1:
                            APPEND current point holder to orderblock storage array decisional
                            
                    # CHECK if it has eniffeciency
                    ELSE IF next current holder close and next next current point holder high is below current point holder low - (((high - low) // 2) * 3):
                            
                        # ORGANIZE where to append
                        IF orderblock storage array extreme is empty and current point holder is higher than structure record pullback index 1:
                            APPEND current point holder to orderblock storage array extreme
                                
                        ELSE IF orderblock storage array decisional is empty and current point holder is equal or below to pullback index 1:
                            APPEND current point holder to orderblock storage array decisional
                
                # CHECK if it has eniffeciency if it is only an ordinary order block
                ELSE IF next current holder close and next next current point holder high is below current point holder low - (((high - low) // 2) * 3):
                            
                    # ORGANIZE where to append
                    IF orderblock storage array extreme is empty and current point holder is higher than structure record pullback index 1:
                        APPEND current point holder to orderblock storage array extreme
                                
                    ELSE IF orderblock storage array decisional is empty and current point holder is equal or below to pullback index 1:
                        APPEND current point holder to orderblock storage array decisional
                                
                # IF above condition filled about extreme orderblock
                IF orderblock storage array extreme is not empty and current point holder is greater than storage structure pullback index 1:
                    SET current point holder to structure record pullback index 1
                    CONTINUE
                        
                # IF above condition filled about decisional orderblock
                IF orderblock storage array decisional is not empty and current point holder is equal or lower than storage structure pullback index 1:
                            
                    # LOOP until the end of the size
                    IF decisional counter is less than length of structure record pullback + 1:
                        SET current point holder to structure record pullback index counter
                        INCREMENT decisional counter 
                        CONTINUE
                            
                #ADVANCE pointers by one if the above condition doesn't satisfies
                SET current point holder to next current point
                SET next current point holder to next next current point
                SET next next current point holder to next next next current point
                CONTINUE
                
    RETURN structure storage array