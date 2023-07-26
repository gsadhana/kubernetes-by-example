const flashcards = document.querySelectorAll('.flashcard');

flashcards.forEach((flashcard) => {
  flashcard.addEventListener('click', function() {
    const isFlipped = this.getAttribute('data-flipped') === 'true';

    if (!isFlipped) {
      this.setAttribute('data-flipped', 'true');
      this.classList.add('flipped');
    } else {
      this.setAttribute('data-flipped', 'false');
      this.classList.remove('flipped');
    }
  });
});