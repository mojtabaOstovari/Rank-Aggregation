# Maximum Value of $\Omega_{Rank}$ on 3D Grid

This Python program computes the maximum value of the function $\Omega_{Rank}(1,1,0, w_{ij}, w_{jk}, w_{ki})$ over a 3D grid in the unit cube [0,1]³.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/mojtabaOstovari/Rank-Aggregation.git
   cd Rank-Aggregation
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the program with the following command:

```bash
python main.py n
```

### Parameters

- **`n`**: Grid size (must be an integer greater than 1)
  - The grid will have `n` points along each axis, resulting in `n³` total points.
  - Runtime complexity: Θ(n²)

### Example

```bash
python main.py 50
```

This will compute the maximum Ω value over a 50×50×50 grid.

### Output

- The maximum value of $\Omega(1, 1, 0, w_{ij}, w_{jk}, w_{ki})$ found over all grid points
- The coordinates $(w_{ij}, w_{jk}, w_{ki})$ where this maximum occurs

## Dependencies

All required Python packages are listed in `requirements.txt`.

## Notes

- The runtime is $(\Theta(n^3))$.
- For accurate results, ensure `n` is sufficiently large to capture the function's behavior.


