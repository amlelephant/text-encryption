#include <iostream>
#include <fstream>
#include <random>
#include <ctime>

using namespace std;

string encrypt_decrypt(const string &text, const string &pad)
{
    string result;
    for (int i = 0; i < text.length(); i++)
    {
        result += text[i] ^ pad[i % pad.length()];
    }
    return result;
}

void save(const string &filename, const string &data)
{
    ofstream file(filename, ios::binary);
    if (file)
    {
        file << data;
        cout << "Data saved to " << filename << " successfully." << endl;
    }
    else
    {
        cerr << "Error: Unable to open file " << filename << " for writing." << endl;
    }
    file.close();
}

string load(string filename)
{
    ifstream file;
    file.open(filename, ios::binary); // Open in binary mode
    string pad;

    if (file)
    {
        // Get the size of the file
        file.seekg(0, ios::end);
        streampos fileSize = file.tellg();
        file.seekg(0, ios::beg);

        // Read the entire contents of the file into the pad string
        pad.resize(fileSize);
        file.read(&pad[0], fileSize);
    }

    file.close();
    return pad;
}

string generate_pad(int length)
{
    const string printable_chars = "0123456789"
                                   "abcdefghijklmnopqrstuvwxyz"
                                   "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                                   "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
                                   "\t\n\r";

    string pad;
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> distribution(0, printable_chars.length() - 1);

    for (int i = 0; i < length; i++)
    {
        pad += printable_chars[distribution(gen)];
    }

    return pad;
}

int main()
{
    string padFilename = "PATH TO PAD";
    string pad = load(padFilename);
    if (pad.empty())
    {
        // Generate a new pad if it doesn't exist
        pad = generate_pad(100);
        save(padFilename, pad);
    }

    string padcheck = load("CHECK FOR CORRECT PAD PATH");
    string result = encrypt_decrypt(padcheck, pad);
    
    save("intended result.txt", result);
    string intendedResult = load("intended result.txt");

    
    
    
    cout << (result == intendedResult) << endl;

    cout << encrypt_decrypt("WHATEVER YOU WANT", pad) << endl;
    save("TXT FILE", encrypt_decrypt("WHATEVER YOU WANT", pad));


    return 0;
}
