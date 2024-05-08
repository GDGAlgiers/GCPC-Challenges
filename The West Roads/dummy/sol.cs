using System;

class Program
{
    static long Solve(long x)
    {
        return x * (x - 1) / 2;
    }

    static void Main(string[] args)
    {
        long x = long.Parse(Console.ReadLine());
        Console.WriteLine(Solve(x));
    }
}
