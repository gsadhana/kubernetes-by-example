const flashcards = document.querySelectorAll('.flashcard-container');

flashcards.forEach((flashcard) => {
  flashcard.addEventListener("click", function() {
    this.classList.toggle("flipped");
  });
});