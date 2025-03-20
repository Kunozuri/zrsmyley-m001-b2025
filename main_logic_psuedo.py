# MAIN LOGIC that is responsible for the whole algorithm
MAIN LOGIC:
    
    # INITIALIZATION of necessary data that is needed
    OPTION of user trading style {
        Positional
        Swing
        Intra-Day
        Scalping
    
    SWITCH trading style:
        
        CASE Positional:
            INITIALIZE high interval = 1W
            INITIALIZE mid interval = 1D
            INITIALIZE low interval = H4
            INITIALIZE entry interval = M15
        
        CASE Swing:
            INITIALIZE high interval = 1D
            INITIALIZE mid interval = H4
            INITIALIZE low interval = H1
            INITIALIZE entry interval = M5
            
        CASE Intra-Day:
            INITIALIZE high interval = H4
            INITIALIZE mid interval = H1
            INITIALIZE low interval = M15
            INITIALIZE entry interval = M1
        
        CASE Scalping:
            INITIALIZE high interval = H1
            INITIALIZE mid interval = M15
            INITIALIZE low interval = M5
            INITIALIZE entry interval = M1
    

    INITIALIZE bollinger bands holder
    INITIALIZE RSI holder
    
    # GET the data of every inteval
    GET 1000 historical candle data of high interval
    GET 1000 historical candle data of mid interval
    GET 1000 historical candle data of low interval
    GET 1000 historical candle data of entry interval
    
    # MOLDING and filtering the noice
    high SCHEMATIC (high interval)
    high SMCstructure (high SCHEMATIC)
    
    mid SCHEMATIC (mid interval)
    mid SMCstructure (mid SCHEMATIC)
    
    low SCHEMATIC (low interval)
    low SMCstructure (low SCHEMATIC)
    
    entry SCHEMATIC (entry interval)
    entry SMCstructure (entry SCHEMATIC)
    
    # GET Technical Analysis on every interval
    Technical Analysis (high SMCstructure, high interval)
    Technical Analysis (mid SMCstructure, mid interval)
    Technical Analysis (low SMCstructure, low interval)
    Technical Analysis (entry SMCstructure, entry interval)
    
    # GET Technical Confluences on every interval
    Trend Channel (high SMCstructure, high interval)
    Trend Channel (mid SMCstructure, mid interval)
    Trend Channel (low SMCstructure, low interval)
    Trend Channel (entry SMCstructure, entry interval)
    
    Support Resistance (high SMCstructure)
    Support Resistance (mid SMCstructure)
    Support Resistance (low SMCstructure)
    Support Resistance (entry SMCstructure)
    
    # GET Technical Indicator Confluences on every interval
    Bollinger Bands (high SMCstructure)
    Bollinger Bands (mid SMCstructure)
    Bollinger Bands (low SMCstructure)
    Bollinger Bands (entry SMCstructure)
    
    RSI (high SMCstructure)
    RSI (mid SMCstructure)
    RSI (low SMCstructure)
    RSI (entry SMCstructure)
    
    # INITIALIZE control flow rhythm
    INITIALIZE static is_TradingALSE
    INITIALIZE static interval filled array [SMCstructure, interval]
    INITIALIZE static price_to_enter
    INITIALIZE static orderblock index
    
    # INITIALIZE order management
    INITIALIZE static stoploss
    INITIALIZE static takeprofit
    INITIALIZE static trailstop
    INITIALIZE static in_open_order to FALSE 
    
    
    # SKIP analysis if already in trade | NOTE: one trade at a time.
    IF is_Trading is False:
        
        # IDENTIFY the current high direction
        
            # IF it tapped the high decisional and extreme orderblock
                # CHECK IF middle orderblock is tapped
                    # CHECK IF within middle and high Bollinger Bands
                        # CHECK middle RSI IF overbought
                            # CHECK IF within high SNR
                                # CHECK IF within high trend channel
                                    SCOB low interval
                                
                                # IF NOT in trend channel
                                    Choch Entry
                                    
                            # IF NOT within high SNR
                                Choch Entry
                         
                # ELSE IF ONLY high orderblock is tapped
                
                    # CHECK IF within high and middle Bollinger Bands
                        # CHECK IF within high SNR
                            # CHECK middle RSI IF overbought
                                # CHECK IF within high SNR
                                    # CHECK IF within high trend channel
                                        SCOB low interval
                                    
                                    # IF NOT in trend channel
                                        Choch Entry
                                    
                                # IF NOT within high SNR
                                    Choch Entry
                                
            # CHECK ELSE IF it tapped the high engineered liquidity
            
                # CHECK IF within low and middle Bollinger Bands
                    # CHECK middle RSI IF overbought 
                        # CHECK IF within high trend channel
                            Choch Entry
            
            
            # CHECK ELSE IF the the current low direction is bearish
            
                # IF it tapped the low decisional and extreme orderblock
                    # CHECK IF within low and middle Bollinger Bands
                        # CHECK low RSI IF overbought
                            # CHECK IF within middle SNR
                                # CHECK IF within middle trend channel
                                    SCOB entry interval
                                    
                                # IF NOT in middle trend channel
                                    Choch Entry
                                        
                            # IF NOT within middle SNR
                                Choch Entry
                                    
                # IF it tapped the middle engineered liquidity
                
                    # CHECK IF within middle and low Bollinger Bands
                        # CHECK low RSI IF oversold
                            # CHECK IF within middle trend channel
                                Choch Entry
            
# NOTE | create here the bearish trend
    
    # IF currently trading
    IF is_Trading:
       
       # CHECK if it has already open order
       IF in_open_order:
           
           # CHECK IF it already had stoploss
           IF stoploss is not empty:
               SWITCH interval filled:
                   CASE low interval:
                       SET trailstop as STOPLOSS(low SMCstructure, orderblock index, trading style, current price, TRUE)
                   
                   CASE middle interval:
                       SET trailstop as STOPLOSS(middle SMCstructure, orderblock index, trading style, current price, TRUE)
                   
                   CASE high interval:
                       SET trailstop as STOPLOSS(high SMCstructure, orderblock index, trading style, current price, TRUE)
             
         # APPLYING the trailstop align to ATR retailing
        IF interval filled SMCstructure trend direction is bullish:
            IF stoploss is lower than trailstop:
                MODIFY the order stoploss
        
        ELSE:
            IF stoploss is above than trailstop:
                MODIFY the order stoploss
                
         # CLOSE order if its overbought and still don't hit the takeprofit
         SWITCH interval filled:
             CASE low interval:
                 # CHECK IF its overbought or oversold even without hitting the takeprofit
                 IF low RSI is overbought or oversold:
                     SET in_open_order to FALSE
                 
                 # CHECK IF it hits the takeprofit
                 IF interval filled SMCstructure trend direction is bullish:
                     IF current price is equal or above takeprofit:
                         SET in_open_order to FALSE
                 
                 ELSE IF interval filled SMCstructure trend direction is bearish:
                     IF current price is equal or below takeprofit:
                         SET in_open_order to FALSE
                 
                 # CLOSE the order because its due? (wudufok am i thinking?)
                 IF not in_open_order:
                     CLOSE the current order
                     SET static is_Trading to FALSE
                     SET static interval filled to NONE
                     SET static price_to_enter to NONE
                     SET static orderblock index to NONE
                     SET static stoploss to NONE
                     SET static takeprofit to NONE
                     SET static in_open_order to FALSE
                     SET is_trading to FALSE
                         
             CASE middle interval:
                 # CHECK IF its overbought or oversold even without hitting the takeprofit
                 IF middle RSI is overbought or oversold:
                     SET in_open_order to FALSE
                 
                 # CHECK IF it hits the takeprofit
                 IF interval filled SMCstructure trend direction is bullish:
                     IF current price is equal or above takeprofit:
                         SET in_open_order to FALSE
                 
                 ELSE IF interval filled SMCstructure trend direction is bearish:
                     IF current price is equal or below takeprofit:
                         SET in_open_order to FALSE
                 
                 # CLOSE the order because its due? (wudufok am i thinking?)
                 IF not in_open_order:
                     CLOSE the current order
                     SET static is_Trading to FALSE
                     SET static interval filled to NONE
                     SET static price_to_enter to NONE
                     SET static orderblock index to NONE
                     SET static stoploss to NONE
                     SET static takeprofit to NONE
                     SET static in_open_order to FALSE
                     SET is_trading to FALSE
                 
             CASE high interval:
                 # CHECK IF its overbought or oversold even without hitting the takeprofit
                 IF high RSI is overbought or oversold:
                     SET in_open_order to FALSE
                 
                 # CHECK IF it hits the takeprofit
                 IF interval filled SMCstructure trend direction is bullish:
                     IF current price is equal or above takeprofit:
                         SET in_open_order to FALSE
                 
                 ELSE IF interval filled SMCstructure trend direction is bearish:
                     IF current price is equal or below takeprofit:
                         SET in_open_order to FALSE
                 
                 # CLOSE the order because its due? (wudufok am i thinking?)
                 IF not in_open_order:
                     CLOSE the current order
                     SET static is_Trading to FALSE
                     SET static interval filled to NONE
                     SET static price_to_enter to NONE
                     SET static orderblock index to NONE
                     SET static stoploss to NONE
                     SET static takeprofit to NONE
                     SET static in_open_order to FALSE
                     SET is_trading to FALSE
        
        # CHECK IF there has no stoploss
        IF stoploss is empty:
            SWITCH interval filled:
                CASE low interval:
                    SET stoploss as STOPLOSS(low SMCstructure, orderblock index, trading style, price to enter, FALSE)
                CASE middle interval:
                    SET stoploss as STOPLOSS(middle SMCstructure, orderblock index, trading style, price to enter, FALSE)
                CASE high interval:
                    SET stoploss as STOPLOSS(high SMCstructure, orderblock index, trading style, price to enter, FALSE)
                    
        # CHECK IF there has no takeprofit
        IF takeprofit is empty:
            SWITCH interval filled:
                CASE low interval:
                    SET takeprofit as TAKE PROFIT (low SMCstructure, low RSI)
                CASE middle interval:
                    SET takeprofit as TAKE PROFIT (middle SMCstructure, middle RSI)
                CASE high interval:
                    SET takeprofit as TAKE PROFIT (high SMCstructure, low RSI)
        
        # EXECUTING the trades
        IF interval filled SMCstructure trend direction is bullish:
            ExecuteTrade(_Symbol, ORDER_TYPE_BUY, lotsize, stoploss, takeprofit)
        ELSE:
            ExecuteTrade(_Symbol, ORDER_TYPE_SELL, lotsize, stoploss, takeprofit)

        SET in_open_order to TRUE
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        # NOTE: this condition is when it tapped and orderblock and try to look for confluences
        # IDENTIFY the current trend direction
        IF high Technical Analysis returned length is not one and direction is bullish:
            
            # REFINEMENT confluence of high and middle interval
            IF current price low is lower than high Technical Analysis index high:
                IF current price low is lower than mid Technical Analysis index high:
                    
                    # CHECK IF Confluence to Bollinger Bands returns True
                    IF mid Bollinger Bands:
                        
                        # CHECK IF there's a validation of trendlines
                        IF current price low is below than Trend Channel next price point and current price close is above Trend Channel next price point:
                            SET price_to_enter as SCOB (mid Technical Analysis index, low interval)
                            
                            # CHECK IF it has an entry point to trade
                            IF price_to_enter is not None:
                                SET is_Trading to True
                                Execute Order (price to enter)
                        
                        # IF not in the zone of trend line
                        ELSE:
                            SET price_to_enter as Choch Entry (mid Technical Analysis index, low interval)
                            
                            # CHECK IF it has an entry point to trade
                            IF price_to_enter is not None:
                                SET is_Trading to True
                                Execute Order (price to enter)
                    
                    # NOTE: if it do not tapped the Bollinger Bands then "NO TRADE"
                    
                # IF it tapped the high Technical Analysis but the mid doesn't then check for Bollinger Bands
                IF mid Bollinger Bands:
                    
                    # CHECK IF there's a validation of trendlines
                    IF current price low is below than Trend Channel next price point and current price close is above Trend Channel next price point:
                        SET price_to_enter as Choch Entry (mid Technical Analysis index, low interval)
                            
                        # CHECK IF it has an entry point to trade
                        IF price_to_enter is not None:
                            SET is_Trading to True
                            Execute Order (price to enter)
                        
                    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





































