# Maximum Omega Function on 3D Grid

This Python program approximates the approximation factor ($\alpha$) of the QuickRank algorithm. As $ \alpha = max_{w_{ij}, w_{jk}, w_{ki}} \frac{\beta\phi_{ijk} + (1-\beta)\mu_{ijk}}{\psi_{ijk}}$, this program computes the maximum value over a 3D grid in the unit cube [0,1]³.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the program with the following command:

```bash
python main.py <n>
```

### Parameters

- **`<n>`**: Grid size (must be an integer greater than 1)
  - The grid will have `n` points along each axis, resulting in `n³` total points.
  - Runtime complexity: Θ(n²)

### Example

```bash
python main.py 50
```

This will compute the maximum Ω value over a 50×50×50 grid.

## Program Details

The program evaluates the function Ω with fixed parameters (1,1,0) and variable weights (w_{ij}, w_{jk}, w_{ki}) at each point in the 3D grid. The grid points are uniformly spaced in the interval [0,1] along each axis.

### Function Signature

The Ω function takes the form:
```
Ω(1, 1, 0, w_{ij}, w_{jk}, w_{ki})
```

### Output

The program outputs:
- The maximum value of Ω found over all grid points
- The coordinates (i, j, k) where this maximum occurs

## Notes

- The runtime scales quadratically with `n` (Θ(n²)).
- For accurate results, ensure `n` is sufficiently large to capture the function's behavior.

## Dependencies

All required Python packages are listed in `requirements.txt`.


## License

[Specify your license here, e.g., MIT, GPL, etc.]
