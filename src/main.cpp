#include <SFML/Graphics.hpp>
// #include <array>

int main() {
    sf::RenderWindow window(sf::VideoMode(200, 200), "SFML works!");
    sf::CircleShape shape(100.f);
    shape.setFillColor(sf::Color::Green);

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) window.close();
        }

        window.clear();
        window.draw(shape);
        window.display();
    }

    sf::FloatRect rect(0, 0, 10, 10);
    rect.getSize();
    rect.getPosition();
    std::array<int, 3> arr = {1, 2, 3};

    return 0;
}
