//Banner Navigation 

//Declare variable for event, standard, weapon banners
const eventBanner = document.querySelector(".banner1");
const standardBanner = document.querySelector(".banner2");
const weaponBanner = document.querySelector(".banner3");
//Declare variable for display-banner
const displayBanner = document.querySelector(".display-banner");
//Add event that outputs specified text into display banner when clicked
//Make anonymous function that navigates to specified banner using arrow notation
eventBanner.addEventListener("click", () => (displayBanner.textContent = "event banner"));
standardBanner.addEventListener("click", () => (displayBanner.textContent = "standard banner"));
weaponBanner.addEventListener("click", () => (displayBanner.textContent = "weapon banner"));