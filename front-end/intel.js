function blinkRed(){
    btyellow = document.getElementById('yellow')
    btgreen = document.getElementById('green')
    btred = document.getElementById('red')
    btred.style.opacity = 1
    btyellow.style.opacity = 0.4
    btgreen.style.opacity = 0.4
}
function blinkYellow(){
    btyellow = document.getElementById('yellow')
    btgreen = document.getElementById('green')
    btred = document.getElementById('red')
    btyellow.style.opacity = 1
    btred.style.opacity = 0.4
    btgreen.style.opacity = 0.4
}
function blinkGreen(){
    btgreen = document.getElementById('green')
    btyellow = document.getElementById('yellow')
    btred = document.getElementById('red')
    btgreen.style.opacity = 1
    btred.style.opacity = 0.4
    btyellow.style.opacity = 0.4
}
function blinkRed2(){
    btyellow = document.getElementById('yellow2')
    btgreen = document.getElementById('green2')
    btred = document.getElementById('red2')
    btred.style.opacity = 1
    btyellow.style.opacity = 0.4
    btgreen.style.opacity = 0.4
}
function blinkYellow2(){
    btyellow = document.getElementById('yellow2')
    btgreen = document.getElementById('green2')
    btred = document.getElementById('red2')
    btyellow.style.opacity = 1
    btred.style.opacity = 0.4
    btgreen.style.opacity = 0.4
}
function blinkGreen2(){
    btgreen = document.getElementById('green2')
    btyellow = document.getElementById('yellow2')
    btred = document.getElementById('red2')
    btgreen.style.opacity = 1
    btred.style.opacity = 0.4
    btyellow.style.opacity = 0.4
}
function blinkRed3(){
    btyellow3 = document.getElementById('yellow3')
    btgreen3 = document.getElementById('green3')
    btred3 = document.getElementById('red3')
    btred3.style.opacity = 1
    btyellow3.style.opacity = 0.4
    btgreen3.style.opacity = 0.4
}
function blinkYellow3(){
    btyellow3 = document.getElementById('yellow3')
    btgreen3 = document.getElementById('green3')
    btred3 = document.getElementById('red3')
    btyellow3.style.opacity = 1
    btred3.style.opacity = 0.4
    btgreen3.style.opacity = 0.4
}
function blinkGreen3(){
    btgreen3 = document.getElementById('green3')
    btyellow3 = document.getElementById('yellow3')
    btred3 = document.getElementById('red3')
    btgreen3.style.opacity = 1
    btred3.style.opacity = 0.4
    btyellow3.style.opacity = 0.4
}
function blinkRed4(){
    btyellow = document.getElementById('yellow4')
    btgreen = document.getElementById('green4')
    btred = document.getElementById('red4')
    btred.style.opacity = 1
    btyellow.style.opacity = 0.4
    btgreen.style.opacity = 0.4
}
function blinkYellow4(){
    btyellow = document.getElementById('yellow4')
    btgreen = document.getElementById('green4')
    btred = document.getElementById('red4')
    btyellow.style.opacity = 1
    btred.style.opacity = 0.4
    btgreen.style.opacity = 0.4
}
function blinkGreen4(){
    btgreen = document.getElementById('green4')
    btyellow = document.getElementById('yellow4')
    btred = document.getElementById('red4')
    btgreen.style.opacity = 1
    btred.style.opacity = 0.4
    btyellow.style.opacity = 0.4
}

function highlights(){
    var l1 = parseInt(document.getElementById("l-1").value)
    var l2 = parseInt(document.getElementById("l-2").value)
    var l3 = parseInt(document.getElementById("l-3").value)
    var l4 = parseInt(document.getElementById("l-4").value)
    var lane1 = document.getElementById("highlight-1")
    var lane2 = document.getElementById("highlight-2")
    var lane3 = document.getElementById("highlight-3")
    var lane4 = document.getElementById("highlight-4")
    var lane = [l1,l2,l3,l4]
    var Lane = [...lane]
    var h1 = Math.max(l1,l2,l3,l4) //max value
    var K = lane.indexOf(h1)
    var k = K+1
    switch(k){
        case 1: 
        lane1.style.backgroundColor = "red"
        lane1.style.opacity = 0.6
        setInterval(function(){blinkLane1()}, 1000)
        break;
        case 2: 
        lane2.style.backgroundColor = "red"
        lane2.style.opacity = 0.6
        setInterval(function(){blinkLane2()}, 1000)
        break;
        case 3: 
        lane3.style.backgroundColor = "red"
        lane3.style.opacity = 0.6
        setInterval(function(){blinkLane3()}, 1000)
        break;
        case 4: 
        lane4.style.backgroundColor = "red"
        lane4.style.opacity = 0.6
        setInterval(function(){blinkLane4()}, 1000)
        break;
    }
    var h4 = Math.min(l1,l2,l3,l4) //min value
    var J = lane.indexOf(h4)
    var j = J+1
    switch(j){
        case 1: 
        lane1.style.backgroundColor = "green"
        lane1.style.opacity = 0.6
        setInterval(function(){blinkLane1()}, 1000)
        break;
        case 2: 
        lane2.style.backgroundColor = "green"
        lane2.style.opacity = 0.6
        setInterval(function(){blinkLane2()}, 1000)
        break;
        case 3: 
        lane3.style.backgroundColor = "green"
        lane3.style.opacity = 0.6
        setInterval(function(){blinkLane3()}, 1000)
        break;
        case 4: 
        lane4.style.backgroundColor = "green"
        lane4.style.opacity = 0.6
        setInterval(function(){blinkLane4()}, 1000)
        break;
    }
    lane.splice(K,1)
    if (K>J){
        lane.splice(J,1)
    }
    else{
        lane.splice(J-1,1)
    }
    console.log(lane)
    // second highest
    h2 = Math.max(lane[0],lane[1])
    a = Lane.indexOf(h2)+1
    console.log(a)
    switch(a){
        case 1: 
        lane1.style.backgroundColor = "orange"
        lane1.style.opacity = 0.6
        setInterval(function(){blinkLane1()}, 1000)
        break;
        case 2: 
        lane2.style.backgroundColor = "orange"
        lane2.style.opacity = 0.6
        setInterval(function(){blinkLane2()}, 1000)
        break;
        case 3: 
        lane3.style.backgroundColor = "orange"
        lane3.style.opacity = 0.6
        setInterval(function(){blinkLane3()}, 1000)
        break;
        case 4: 
        lane4.style.backgroundColor = "orange"
        lane4.style.opacity = 0.6
        setInterval(function(){blinkLane4()}, 1000)
        break;
    }
    h3 = Math.min(lane[0],lane[1])
    b = Lane.indexOf(h3)+1
    switch(b){
        case 1: 
        lane1.style.backgroundColor = "yellow"
        lane1.style.opacity = 0.6
        setInterval(function(){blinkLane1()}, 1000)
        
        break;
        case 2: 
        lane2.style.backgroundColor = "yellow"
        lane2.style.opacity = 0.6
        setInterval(function(){blinkLane2()}, 1000)
        break;
        case 3: 
        lane3.style.backgroundColor = "yellow"
        lane3.style.opacity = 0.6
        setInterval(function(){blinkLane3()}, 1000)
        break;
        case 4: 
        lane4.style.backgroundColor = "yellow"
        lane4.style.opacity = 0.6
        setInterval(function(){blinkLane4()}, 1000)
        break;
    }
    function blinkLane1(){
            lane1.style.opacity = 0.6
            setTimeout(function(){lane1.style.opacity = 0.8}, 500)
    }
    function blinkLane2(){
            lane2.style.opacity = 0.6
            setTimeout(function(){lane2.style.opacity = 0.8}, 500)
    }
    function blinkLane3(){
            lane3.style.opacity = 0.6
            setTimeout(function(){lane3.style.opacity = 0.8}, 500)
    }
    function blinkLane4(){
            lane4.style.opacity = 0.6
            setTimeout(function(){lane4.style.opacity = 0.8}, 500)
    }
}