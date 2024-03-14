function ageTeller (dob){
    const currentDate = new Date();
    const currentYear = currentDate.getFullYear();
    console.log(`your age is ${currentYear-dob}`);
}

ageTeller(1992)
