/*
    Lenguajes de programacion 1.
    Daniel Robayo 18-11086.

    Pregunta 1, parte b.
*/
import std.stdio;
import std.conv;
import core.exception;
import std.string;

string usage_message = "usage: ./matrix n < input_file";

void main (string[] args)
{
    int n;
    int[] row;
    int[][] m, m_trans, res;
    string input;
    string[] input_row;

    try 
    {   
        input = readln();
        n = parse!int(input);
        
        m.length = n;
        row.length = n;
        
        for (int i=0; i<n; i++)
        {   
            input_row = split(readln(), " ");
            for (int j=0; j<n; j++)
            {
                row[j] = parse!int(input_row[j]);
            }
            m[i].length = n;
            m[i][0..n] = row;
        }
        
        m_trans = transpose(m, n);  
        res = mutl_matrix(m, m_trans, n);

        for (int i=0; i<n; i++) 
        {
            writeln(res[i]);
        }

    }
    catch(ArrayIndexError e)
    {
        writeln(usage_message, "| tamano de input incorrecto");
    }
    catch(ConvException e)
    {
        writeln(usage_message, "| n debe ser un entero");
    }
    catch(AssertError e)
    {
        writeln(usage_message, "| n debe ser mayor o igual que cero | error en input");
    }
    finally
    {
        writeln("-----");
    }
}

int[][] transpose(int[][] m, int n) 
{   
    int [][] trans;
    trans.length = n;
    for (int i=0; i<n; i++) 
    {
        trans[i].length = n;
    }

    for (int i=0; i<n; i++)
    {
        for (int j=0; j<n; j++)
        {
            trans[i][j] = m[j][i];
        }
    }
    return trans;
}

int[][] mutl_matrix(int[][] a, int[][] b, int n)
{
    int[][] mult;
    int val;

    mult.length = n;
    for (int i; i<n; i++)
    {
        mult[i].length = n;
    }

    for (int i=0; i<n; i++)
    {
        for (int j=0; j<n; j++)
        {
            val = 0;
            for (int k=0; k<n; k++)
            {
                val += (a[i][k]*b[k][j]);
            }
            mult[i][j] = val;
        }
    }
    return mult;
}