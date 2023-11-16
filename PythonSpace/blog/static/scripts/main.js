// let myHeading = document.querySelector("h1");
// myHeading.textContent = "Hello world!";

// let iceCream = "chocolate";
// if (iceCream === "chocolate") {
//   alert("我最喜欢巧克力冰激淋了。");
// } else {
//   alert("但是巧克力才是我的最爱呀……");
// }


// let cheese = "Cheddar";

// if (cheese) {
//   console.log("耶！这里有一些制作奶酪吐司的奶酪。");
// } else {
//   console.log("今天你的吐司上没有奶酪了。");
// }

// const contacts = [
//   "Chris:2232322",
//   "Sarah:3453456",
//   "Bill:7654322",
//   "Mary:9998769",
//   "Dianne:9384975",
// ];
// const para = document.querySelector("p");
// const input = document.querySelector("input");
// const btn = document.querySelector("button");

// btn.addEventListener("click", function () {
//   let searchName = input.value.toLowerCase();
//   input.value = "";
//   input.focus();
//   for (let i = 0; i < contacts.length; i++) {
//     let splitContact = contacts[i].split(":");
//     if (splitContact[0].toLowerCase() === searchName) {
//       para.textContent =
//         splitContact[0] + "'s number is " + splitContact[1] + ".";
//       break;
//     } else if (i === contacts.length - 1) {
//       para.textContent = "Contact not found.";
//     }
//   }
// });

input.onchange = function () {
  var num = input.value;
  if (isNaN(num)) {
    para.textContent = "You need to enter a number!";
  } else {
    para.textContent =
      num +
      " squared is " +
      squared(num) +
      ". " +
      num +
      " cubed is " +
      cubed(num) +
      ". " +
      num +
      " factorial is " +
      factorial(num) +
      ".";
  }
};
