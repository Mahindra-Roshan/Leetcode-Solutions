/* Sudoku App */
(function() {
  "use strict";

  /**
   * Board representation uses a flat array of length 81 with values 0-9
   * 0 means empty. Index mapping: row * 9 + col
   */
  const SIZE = 9;
  const BOX = 3;

  /** @type {number[]} */
  let board = new Array(81).fill(0);
  /** @type {boolean[]} */
  let fixed = new Array(81).fill(false);
  /** @type {Set<number>[]} */
  let notes = Array.from({ length: 81 }, () => new Set());
  let selectedIndex = -1;
  let notesMode = false;

  const elBoard = document.getElementById("board");
  const elStatus = document.getElementById("status");
  const elSolve = document.getElementById("solve");
  const elCheck = document.getElementById("check");
  const elClear = document.getElementById("clear");
  const elNotesToggle = document.getElementById("notes-toggle");

  function setStatus(text, type = "") {
    elStatus.textContent = text;
    elStatus.dataset.type = type;
  }

  function coordsToIndex(row, col) { return row * SIZE + col; }
  function indexToCoords(index) { return [Math.floor(index / SIZE), index % SIZE]; }

  function getRowValues(row) {
    const values = new Set();
    for (let col = 0; col < SIZE; col++) {
      const v = board[coordsToIndex(row, col)];
      if (v) values.add(v);
    }
    return values;
  }

  function getColValues(col) {
    const values = new Set();
    for (let row = 0; row < SIZE; row++) {
      const v = board[coordsToIndex(row, col)];
      if (v) values.add(v);
    }
    return values;
  }

  function getBoxValues(row, col) {
    const values = new Set();
    const r0 = Math.floor(row / BOX) * BOX;
    const c0 = Math.floor(col / BOX) * BOX;
    for (let r = r0; r < r0 + BOX; r++) {
      for (let c = c0; c < c0 + BOX; c++) {
        const v = board[coordsToIndex(r, c)];
        if (v) values.add(v);
      }
    }
    return values;
  }

  function getConflicts(index, value) {
    if (!value) return [];
    const [row, col] = indexToCoords(index);
    const conflicts = [];
    for (let c = 0; c < SIZE; c++) {
      const i = coordsToIndex(row, c);
      if (i !== index && board[i] === value) conflicts.push(i);
    }
    for (let r = 0; r < SIZE; r++) {
      const i = coordsToIndex(r, col);
      if (i !== index && board[i] === value) conflicts.push(i);
    }
    const r0 = Math.floor(row / BOX) * BOX;
    const c0 = Math.floor(col / BOX) * BOX;
    for (let r = r0; r < r0 + BOX; r++) {
      for (let c = c0; c < c0 + BOX; c++) {
        const i = coordsToIndex(r, c);
        if (i !== index && board[i] === value) conflicts.push(i);
      }
    }
    return Array.from(new Set(conflicts));
  }

  function isValidMove(index, value) {
    if (value === 0) return true;
    const [row, col] = indexToCoords(index);
    return !getRowValues(row).has(value)
        && !getColValues(col).has(value)
        && !getBoxValues(row, col).has(value);
  }

  function findEmptyIndex() {
    for (let i = 0; i < 81; i++) if (board[i] === 0) return i;
    return -1;
  }

  function getCandidates(index) {
    const [row, col] = indexToCoords(index);
    const used = new Set([...getRowValues(row), ...getColValues(col), ...getBoxValues(row, col)]);
    const candidates = [];
    for (let v = 1; v <= 9; v++) if (!used.has(v)) candidates.push(v);
    return candidates;
  }

  // Backtracking solver
  function solve(depth = 0) {
    const i = findEmptyIndex();
    if (i === -1) return true;
    const candidates = getCandidates(i);
    // Heuristic: try smaller candidate sets first by choosing min remaining values
    // Already choosing the first empty cell; to improve, gather all empties and pick min MRV
    // Simple approach for now: sort candidates randomly to vary generation
    for (const v of candidates) {
      if (isValidMove(i, v)) {
        board[i] = v;
        if (solve(depth + 1)) return true;
        board[i] = 0;
      }
    }
    return false;
  }

  function clone(arr) { return arr.slice(); }

  // Count solutions with backtracking (stop at >1)
  function countSolutions(limit = 2) {
    let numSolutions = 0;
    const snapshot = clone(board);
    function backtrack() {
      const i = findEmptyIndex();
      if (i === -1) { numSolutions++; return numSolutions < limit; }
      const candidates = getCandidates(i);
      for (const v of candidates) {
        if (isValidMove(i, v)) {
          board[i] = v;
          if (!backtrack()) return false; // early stop if reached limit
          board[i] = 0;
        }
      }
      return true;
    }
    backtrack();
    for (let i = 0; i < 81; i++) board[i] = snapshot[i];
    return numSolutions;
  }

  // Generate a full valid board then remove cells ensuring uniqueness
  function generateCompletedBoard() {
    board = new Array(81).fill(0);
    // Seed with a random permutation in the first row to vary
    const nums = [1,2,3,4,5,6,7,8,9].sort(() => Math.random() - 0.5);
    for (let c = 0; c < 9; c++) board[c] = nums[c];
    solve();
  }

  function generatePuzzle(difficulty = "easy") {
    generateCompletedBoard();
    const solution = clone(board);
    // Remove cells based on difficulty, while keeping unique solution
    const indices = Array.from({ length: 81 }, (_, i) => i).sort(() => Math.random() - 0.5);
    const removalsByDifficulty = { easy: 40, medium: 50, hard: 58 };
    const targetRemovals = removalsByDifficulty[difficulty] || removalsByDifficulty.easy;
    let removed = 0;
    for (const idx of indices) {
      const backup = board[idx];
      board[idx] = 0;
      const solCount = countSolutions(2);
      if (solCount !== 1) {
        board[idx] = backup; // revert, not unique
      } else {
        removed++;
      }
      if (removed >= targetRemovals) break;
    }
    // Build fixed cells from current board
    fixed = board.map(v => v !== 0);
    notes = Array.from({ length: 81 }, () => new Set());
    render();
    setStatus(`New ${difficulty} puzzle generated.`);
  }

  function render() {
    elBoard.innerHTML = "";
    for (let i = 0; i < 81; i++) {
      const value = board[i];
      const isFixed = fixed[i];
      const cell = document.createElement("div");
      cell.className = "cell";
      cell.setAttribute("role", "gridcell");
      cell.dataset.index = String(i);
      cell.dataset.fixed = String(isFixed);
      cell.tabIndex = 0;

      const conflicts = getConflicts(i, value);
      if (conflicts.length > 0) cell.dataset.conflict = "true";

      if (value) {
        cell.textContent = String(value);
      } else {
        const noteContainer = document.createElement("div");
        noteContainer.className = "notes";
        for (let n = 1; n <= 9; n++) {
          const span = document.createElement("div");
          span.className = "note";
          span.textContent = notes[i].has(n) ? String(n) : "";
          noteContainer.appendChild(span);
        }
        cell.appendChild(noteContainer);
      }

      if (i === selectedIndex) cell.dataset.selected = "true";

      cell.addEventListener("click", () => selectCell(i));
      cell.addEventListener("keydown", handleCellKeydown);
      elBoard.appendChild(cell);
    }
  }

  function selectCell(index) {
    selectedIndex = index;
    render();
  }

  function handleCellKeydown(event) {
    const index = Number(event.currentTarget.dataset.index);
    if (event.key >= "1" && event.key <= "9") {
      inputValue(index, Number(event.key));
      event.preventDefault();
      return;
    }
    if (event.key === "Backspace" || event.key === "Delete" || event.key === "0") {
      inputValue(index, 0);
      event.preventDefault();
      return;
    }
    const [row, col] = indexToCoords(index);
    if (event.key === "ArrowUp" && row > 0) selectCell(coordsToIndex(row - 1, col));
    if (event.key === "ArrowDown" && row < 8) selectCell(coordsToIndex(row + 1, col));
    if (event.key === "ArrowLeft" && col > 0) selectCell(coordsToIndex(row, col - 1));
    if (event.key === "ArrowRight" && col < 8) selectCell(coordsToIndex(row, col + 1));
  }

  function inputValue(index, value) {
    if (fixed[index]) return;
    if (notesMode && value !== 0) {
      if (notes[index].has(value)) notes[index].delete(value); else notes[index].add(value);
    } else {
      notes[index].clear();
      if (isValidMove(index, value)) {
        board[index] = value;
        setStatus(value ? `Placed ${value}.` : "Cleared cell.");
      } else if (value === 0) {
        board[index] = 0;
        setStatus("Cleared cell.");
      } else {
        board[index] = value; // still place to show conflict visually
        setStatus("Conflict detected.", "warn");
      }
    }
    render();
  }

  function handleKeypad(event) {
    const target = event.target.closest(".key");
    if (!target) return;
    const key = target.dataset.key;
    if (selectedIndex === -1) return setStatus("Select a cell first.", "warn");
    if (key === "erase") { inputValue(selectedIndex, 0); return; }
    const value = Number(key);
    if (value >= 1 && value <= 9) inputValue(selectedIndex, value);
  }

  function handleCheck() {
    for (let i = 0; i < 81; i++) {
      const v = board[i];
      if (v === 0) { setStatus("There are empty cells.", "warn"); return; }
      const conflicts = getConflicts(i, v);
      if (conflicts.length > 0) { setStatus("There are conflicts.", "warn"); return; }
    }
    setStatus("Looks valid so far!", "ok");
  }

  function handleSolve() {
    const snapshot = clone(board);
    if (solve()) {
      setStatus("Solved.");
      // lock all as fixed after solve
      fixed = board.map(v => v !== 0);
      render();
    } else {
      for (let i = 0; i < 81; i++) board[i] = snapshot[i];
      setStatus("No solution found.", "warn");
    }
  }

  function handleClear() {
    for (let i = 0; i < 81; i++) if (!fixed[i]) board[i] = 0;
    notes = Array.from({ length: 81 }, () => new Set());
    render();
    setStatus("Cleared non-fixed cells.");
  }

  function bindControls() {
    document.querySelector(".keypad").addEventListener("click", handleKeypad);
    elCheck.addEventListener("click", handleCheck);
    elSolve.addEventListener("click", handleSolve);
    elClear.addEventListener("click", handleClear);
    elNotesToggle.addEventListener("change", () => { notesMode = elNotesToggle.checked; setStatus(notesMode ? "Notes enabled." : "Notes disabled."); });
    document.getElementById("new-easy").addEventListener("click", () => generatePuzzle("easy"));
    document.getElementById("new-medium").addEventListener("click", () => generatePuzzle("medium"));
    document.getElementById("new-hard").addEventListener("click", () => generatePuzzle("hard"));
  }

  // init
  bindControls();
  generatePuzzle("easy");
})();

