#include<iostream>
#include<string>
#include<thread>
#include<chrono>

// https://stackoverflow.com/questions/6649936/c-compiling-on-windows-and-linux-ifdef-switch
#ifdef _WIN32
// https://stackoverflow.com/questions/6486289/how-can-i-clear-console
// se non funziona lamentati con stackoverflow
void clear() {
    COORD topLeft  = { 0, 0 };
    HANDLE console = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_SCREEN_BUFFER_INFO screen;
    DWORD written;

    GetConsoleScreenBufferInfo(console, &screen);
    FillConsoleOutputCharacterA(
        console, ' ', screen.dwSize.X * screen.dwSize.Y, topLeft, &written
    );
    FillConsoleOutputAttribute(
        console, FOREGROUND_GREEN | FOREGROUND_RED | FOREGROUND_BLUE,
        screen.dwSize.X * screen.dwSize.Y, topLeft, &written
    );
    SetConsoleCursorPosition(console, topLeft);
}
#else
// assumes posix if not windows
// https://stackoverflow.com/questions/6486289/how-can-i-clear-console
// (same link as above)
void clear() {
    // CSI[2J clears screen, CSI[H moves the cursor to top-left corner
    std::cout << "\x1B[2J\x1B[H";
}

#endif

class Cazzodrawer {
private:
    const std::string cazzo_base[8] = {"  +-------+   +-------+   ",
                                       " /          +          \\",
                                       "|           |           |",
                                       "|           |           |",
                                       "|           |           |",
                                       " \\                     /",
                                       "  +- -      +      - -+  ",
                                       "   +--             --+  "};

    const std::string cazzo_extender="    |               |";

    const std::string cazzo_cima[7]= {"    +--           --+  ",
                                      "   /                 \\",
                                      "   |                 | ",
                                      "   \\                 /",
                                      "    \\       |       / ",
                                      "     +------|------+   "};

public:
    void draw_cazzo(int l) {
        /* disegna un cazzo lungo `l` sul terminale

           @param l lunghezza del cazzo
        */
        for(std::string s : Cazzodrawer::cazzo_base) {
            std::cout<<s<<'\n';
        }

        for(int i = 0; i<l; ++i) {
            std::cout<<Cazzodrawer::cazzo_extender<<'\n';
        }

        for(std::string s : Cazzodrawer::cazzo_cima) {
            std::cout<<s<<'\n';
        }
    }

    void loop_cazzo(int min_len, int max_len, int millis) {
        while(true) {
            for(int i = min_len; i<max_len; ++i) {
                draw_cazzo(i);
                std::this_thread::sleep_for(std::chrono::milliseconds(millis));
                clear();
            }

            for(int i = max_len; i>min_len; --i) {
                draw_cazzo(i);
                std::this_thread::sleep_for(std::chrono::milliseconds(millis));
                clear();
            }
        } 
    }
};

int main(int argc, char** argv) {
    Cazzodrawer a = Cazzodrawer();
    switch(argc) {
    case 2:
        a.draw_cazzo(std::stoi(argv[1]));
        break;
    case 3:
        a.loop_cazzo(std::stoi(argv[1]), std::stoi(argv[2]), 50);
        break;
    case 4:
        a.loop_cazzo(std::stoi(argv[1]), std::stoi(argv[2]), std::stoi(argv[3]));
        break;
    default:
        std::cerr<<"porcoddio";
        return 1;
    }
    return 0;
}
