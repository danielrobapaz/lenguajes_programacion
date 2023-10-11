import std.stdio;
import std.conv;
import core.exception;
import std.string;

string usage_message = "usage: ./rotar [string_to_rotate] n_chars_to_rotate ";

void main(string[] args)
{   
    string string_to_rotate;
    int n_chars_to_rotate;

    try 
    {   
        
        if (args.length == 2){
            string_to_rotate = "";
            n_chars_to_rotate = to!int(args[1]);
        } 
        else 
        {
            string_to_rotate = args[1];
            n_chars_to_rotate = to!int(args[2]);
        }
        
        assert(n_chars_to_rotate >= 0);

        writeln(rotar(string_to_rotate, n_chars_to_rotate));  

    }
    catch(ArrayIndexError e)
    {
        writeln(usage_message, "| tamano de input incorrecto");
    }
    catch(ConvException e)
    {
        writeln(usage_message, "| n_chars_to_rotate debe ser un entero");
    }
    catch(AssertError e)
    {
        writeln(usage_message, "| n_chars_to_rotate debe ser mayor o igual que cero");
    }
    finally
    {
        writeln("-----");
    }

}

string rotar(string w, int k) 
{
    if (w == "" || k == 0)
    {
        return w;
    } 
    return rotar(w[1..$]~w[0], k-1);;
}