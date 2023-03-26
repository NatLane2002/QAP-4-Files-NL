/*
Description: Javascript portion of QAP 4

Author: Nathaniel Lane
Date: March 17th, 2023
*/

// Create a reasonably complicated object using javascript
const customer = {
    firstName: "Nathaniel",
    lastName: "Lane",
    birthDate: "12-29-2002",
    gender: "Male",
    roomPref: ["24 degrees celsius", "Bright", "Mini Fridge", "TV"],
    paymentMethod: "Credit Card",
    mailingAddress: {
        strAdd: "6 Peronne Road",
        city: "Grand-Falls Windsor",
        province: "NL",
        posCode: "A2A2B2",
    },
    phoneNum: "(709)-572-4205",
    dates: {
        checkIn: "03-20-2023",
        checkOut: "03-24-2023",
    },
    vehicleMake: "Honda",
    occupation: "Software Developer",
    favouriteFoods: ["Pizza", "Aero Bars", "Burgers",  "Chicken"],
    getAge() {
        const birthDate = new Date(this.birthDate);
        const now = new Date();
        let age = now.getFullYear() - birthDate.getFullYear();
        const monthDiff = now.getMonth() - birthDate.getMonth();
        if (monthDiff < 0 || (monthDiff === 0 && now.getDate() < birthDate.getDate())) {
            age--;
        }
        return age;
    },
    getDurationOfStay() {
        return (new Date(this.dates.checkOut) - new Date(this.dates.checkIn)) / (1000 * 60 * 60 * 24);
    }
};

// Create a template literal describing the customer object
const customerInfo = `<p>Meet our motel customer, ${customer.firstName} ${customer.lastName}! ${customer.gender === "Male" ? "He" : "She"} is ${customer.getAge()} years old and will be staying with us from ${customer.dates.checkIn} to ${customer.dates.checkOut}, which is a duration of ${customer.getDurationOfStay()} days.</p> <p>${customer.gender === "Male" ? "He" : "She"} prefers a room temperature of ${customer.roomPref[0]} and likes ${customer.roomPref[1].toLowerCase()} lighting. ${customer.gender === "Male" ? "He" : "She"} also requested a mini fridge and TV in the room. ${customer.firstName} will be paying with ${customer.paymentMethod}.</p> <p>Here is ${customer.gender === "Male" ? "his" : "her"} mailing address: ${customer.mailingAddress.strAdd}, ${customer.mailingAddress.city}, ${customer.mailingAddress.province} ${customer.mailingAddress.posCode}. If you need to contact ${customer.firstName}, ${customer.gender === "Male" ? "his" : "her"} phone number is ${customer.phoneNum}.</p> <p>${customer.firstName} drives a ${customer.vehicleMake} and works as a ${customer.occupation.toLowerCase()}. ${customer.gender === "Male" ? "His" : "Her"} favourite foods include ${customer.favouriteFoods.join(", ").toLowerCase()}.</p>`;

// Find a way to get my template literal to show up on my webpage
window.onload = function() {
    const customerInfoDiv = document.getElementById("customer-info");
    customerInfoDiv.innerHTML = customerInfo;
  };