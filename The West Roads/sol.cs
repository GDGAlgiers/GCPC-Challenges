using System;

class Program
{
    static int Solve(int x)
    {
        return x * (x - 1) / 2;
    }

    static void Main(string[] args)
    {
        int x = int.Parse(Console.ReadLine());
        Console.WriteLine(Solve(x));
    }
}