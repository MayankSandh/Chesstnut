// JavaScript code for handling a basic chess game

// Function to create the chessboard and place initial pieces
function createChessboard() {
  const chessboard = document.getElementById('chessboard');
  let isBlack = false;

  for (let row = 0; row < 8; row++) {
    isBlack = !isBlack;

    for (let col = 0; col < 8; col++) {
      const square = document.createElement('div');
      square.classList.add('square');
      square.classList.add((isBlack ? 'black' : 'white'));
      square.dataset.row = row;
      square.dataset.col = col;

      chessboard.appendChild(square);
      isBlack = !isBlack;
    }
  }

  // Add initial pieces to the chessboard
  placeInitialPieces();
}

// Function to place initial pieces on the chessboard
function placeInitialPieces() {
  const squares = document.querySelectorAll('.square');

  squares.forEach(square => {
    const row = parseInt(square.dataset.row);
    const col = parseInt(square.dataset.col);

    if ((row === 0 || row === 1 || row === 6 || row === 7)) {
      const piece = document.createElement('img');
      piece.classList.add('piece');
      piece.draggable = true;

      if (row === 0 || row === 7) {
        switch (col) {
          case 0:
          case 7:
            piece.src = `pieces/r_${row === 0 ? 'b' : 'w'}.svg`;
            break;
          case 1:
          case 6:
            piece.src = `pieces/n_${row === 0 ? 'b' : 'w'}.svg`;
            break;
          case 2:
          case 5:
            piece.src = `pieces/b_${row === 0 ? 'b' : 'w'}.svg`;
            break;
          case 3:
            piece.src = `pieces/q_${row === 0 ? 'b' : 'w'}.svg`;
            break;
          case 4:
            piece.src = `pieces/k_${row === 0 ? 'b' : 'w'}.svg`;
            break;
          default:
            break;
        }
      } else {
        piece.src = `pieces/p_${row === 1 ? 'b' : 'w'}.svg`;
      }

      square.appendChild(piece);
    }
  });

  // Enable drag-and-drop functionality after placing pieces
  handleDragAndDrop();
}

// Function to check if the move to a square is valid
function isValidSquare(startRow, startCol, endRow, endCol, pieceType) {
  // Implement your logic here to validate the move based on the piece type and positions
  // Return true if the move is valid; otherwise, return false

  // For example, let's assume a pawn's movement where it can only move one step forward
  if (pieceType === 'p') {
    const direction = (pieceType === 'p' && piece.src.includes('w')) ? 1 : -1; // Assuming white pawns move upward

    if (startCol === endCol && endRow - startRow === direction) {
      return true;
    }
  }

  // Add more logic for other pieces' movements as needed

  return false;
}

// Function to handle drag-and-drop functionality for pieces
function handleDragAndDrop() {
  const pieces = document.querySelectorAll('.piece');

  pieces.forEach(piece => {
    piece.addEventListener('dragstart', dragStart);
    piece.addEventListener('dragend', dragEnd);
  });

  const squares = document.querySelectorAll('.square');

  squares.forEach(square => {
    square.addEventListener('dragover', dragOver);
    square.addEventListener('dragenter', dragEnter);
    square.addEventListener('dragleave', dragLeave);
    square.addEventListener('drop', dragDrop);
  });
}

function dragStart(event) {
  event.dataTransfer.setData('text/plain', event.target.parentElement.dataset.row + ',' + event.target.parentElement.dataset.col);
  setTimeout(() => {
    event.target.style.display = 'none';
  }, 0);
}

function dragEnd() {
  this.style.display = 'block';
}

function dragOver(event) {
  event.preventDefault();
}

function dragEnter(event) {
  event.preventDefault();
}

function dragLeave() {
  // Add any desired visual feedback when leaving the drop area
}

function dragDrop(event) {
  event.preventDefault();
  const data = event.dataTransfer.getData('text/plain');
  const [startRow, startCol] = data.split(',');
  const draggedPiece = document.querySelector(`[data-row="${startRow}"][data-col="${startCol}"] img`);
  const targetSquare = event.target.tagName.toLowerCase() === 'img' ? event.target.parentElement : event.target;
  const endRow = parseInt(targetSquare.dataset.row);
  const endCol = parseInt(targetSquare.dataset.col);
  const pieceType = draggedPiece.src.split('/').pop().split('_')[1][0]; // Extracting piece type from the image source

  if (isValidSquare(parseInt(startRow), parseInt(startCol), endRow, endCol, pieceType)) {
    if (targetSquare.hasChildNodes()) {
      const capturedPiece = targetSquare.querySelector('img');
      capturedPiece.remove();
    }
    targetSquare.appendChild(draggedPiece);
  } else {
    // Move is invalid, handle accordingly (e.g., show an alert or do nothing)
    console.log('Invalid move');
  }
}

// Create the chessboard and place pieces when the page loads
document.addEventListener('DOMContentLoaded', () => {
  createChessboard();
});
