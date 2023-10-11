import std.stdio;
import std.conv;
import core.exception;
import std.string;

string usage_message = "usage: ./matrix n ";

void main (string[] args)
{
    int n;

    try 
    {   
        n = to!int(args[1]);
        assert(n > 0);

        writeln(n);  

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
        writeln(usage_message, "| n debe ser mayor o igual que cero");
    }
    finally
    {
        writeln("-----");
    }
}