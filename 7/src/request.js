const request = () => {
  return new Promise((resolve, reject) => {
    const random = Math.floor(Math.random() * 2);

    setTimeout(() => {
      if (random) {
        resolve({ data: "success message" });
      } else {
        reject(new Error("error message"));
      }
    }, 2000);
  });
};

module.exports = request;
