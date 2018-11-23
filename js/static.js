document.custom  = {

    "colors" : ["white","silver",
                "grey","red",
                "maroon","yellow",
                "olive","lime",
                "green","aqua",
                "teal","blue",
                "navy","fuchsia",
                "purple"
            ],
    
    "themes":  [ {"Crime Doesn’t Pay" :{} },
            {"Own Worst Enemy":{}},
            {"Coming of Age":{}},
            {"Death":{}},
            {"Overcoming the Odds":{}},
            {"Capitalism":{}},
            {"Technology":{}},
            {"Love conquers all":{}},
            {"Religion":{}},
            {"Humanity vs. nature":{}},
            {"The individual vs. society":{}},
            {"Family":{}},
            {"Good vs. evil":{}},
            {"War":{}}],

            generateRandRGB:   function() { return Math.floor(Math.random() * 256) },
            currentTimeStamp:  function(){ return new Date()},
            generateSignature: function() {

                                   returnArray = []
                                   for(var i = 0;i < 9;i++) {
                
                                       returnArray.push( document.custom.generateRandRGB() )
                                   }
                                    return returnArray
                                },
            alphabet:['a','b','c','d','e','f','e','g','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
            digits:['0','1','2','3','4','5','6','7','8','9'],
            randDigit: function() { return Math.floor(Math.random() + 10)},
            spanCount:0,
            addSpan:function() {
                document.custom.spanCount=  document.custom.spanCount + 1
                span_new    = document.createElement("SPAN")
                span_new.id = document.custom.spanCount;
                document.body.appendChild(span_new)
                
            },
            arrayToSpans: function(inputArray) {
                
            }
        }      