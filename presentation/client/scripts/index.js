const counter = document.getElementById("counter");

let updateCounter = async () => {
  const data = await fetch("https://api.countapi.xyz/hit/onVaCourir/visits");
  const count = await data.json();
  counter.innerHTML = count.value;
  counter.style.filter = "blur(0)";
  console.log(count.value);
};

updateCounter();
