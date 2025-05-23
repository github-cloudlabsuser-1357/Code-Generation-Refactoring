class Calculator {
    add(a, b) {
        return a + b;
    }

    subtract(a, b) {
        return a - b;
    }

    multiply(a, b) {
        return a * b;
    }

    divide(a, b) {
        if (b === 0) {
            throw new Error("Cannot divide by zero");
        }
        return a / b
    }
    modulus(a, b) {
        if (b === 0) {
            throw new Error("Cannot divide by zero");
        }
        return a % b;
    }
    power(a, b) {
        return Math.pow(a, b);
    }
    squareRoot(a) {
        if (a < 0) {
            throw new Error("Cannot take square root of negative number");
        }
        return Math.sqrt(a);
    }
    factorial(n) {
        if (n < 0) {
            throw new Error("Cannot take factorial of negative number");
        }
        if (n === 0 || n === 1) {
            return 1;
        }
        let result = 1;
        for (let i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
    fibonacci(n) {
        if (n < 0) {
            throw new Error("Cannot calculate Fibonacci of negative number");
        }
        const fib = [0, 1];
        for (let i = 2; i <= n; i++) {
            fib[i] = fib[i - 1] + fib[i - 2];
        }
        return fib[n];
    }
    gcd(a, b) {
        if (b === 0) {
            return a;
        }
        return this.gcd(b, a % b);
    }
    lcm(a, b) {
        if (a === 0 || b === 0) {
            return 0;
        }
        return Math.abs(a * b) / this.gcd(a, b);
    }
    average(arr) {
        if (arr.length === 0) {
            throw new Error("Cannot calculate average of empty array");
        }
        const sum = arr.reduce((acc, val) => acc + val, 0);
        return sum / arr.length;
    }
            
}