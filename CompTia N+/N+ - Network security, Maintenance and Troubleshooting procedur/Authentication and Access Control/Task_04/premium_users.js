
// Array of user objects
const users = [
    {
        username: "Rahul",
        isPremium: true,
        lastLogin: "2024-06-08"
    },
    {
        username: "Amit",
        isPremium: false,
        lastLogin: "2024-06-09"
    },
    {
        username: "Priya",
        isPremium: true,
        lastLogin: "2024-06-01"
    },
    {
        username: "Neha",
        isPremium: true,
        lastLogin: "2024-06-05"
    },
    {
        username: "Karan",
        isPremium: true,
        lastLogin: "2024-06-10"
    }
];

// Today's date
const today = new Date("2024-06-10");

// Function to filter premium users
function getPremiumUsers(users) {

    return users.filter(user => {

        const lastLogin = new Date(user.lastLogin);

        const daysDifference =
            (today - lastLogin) / (1000 * 60 * 60 * 24);

        return user.isPremium === true &&
               daysDifference >= 0 &&
               daysDifference <= 7;
    });
}

// Display filtered users
const result = getPremiumUsers(users);

console.log("Premium Users Logged In Within Last 7 Days:");
console.log(result);
