window.addEventListener("load", function() {
  const flashcards = document.querySelectorAll(".flashcard");

  flashcards.forEach((flashcard) => {
    flashcard.addEventListener("click", function() {
      this.classList.toggle("flipped");
    });
  });
});