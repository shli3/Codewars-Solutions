var countBits = function(n) {
  
  var counter = 0;
  //console.log(n)

  while(n >= 1)
  {
    
    if(Math.floor(n) % 2 == 1) counter++;
    n = n / 2;
         
  }
  
  return counter;
};
