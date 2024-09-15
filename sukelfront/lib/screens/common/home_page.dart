import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('SUKELAGRI'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/login');
              },
              child: const Text('Se connecter'),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/productor/home');
              },
              child: const Text('Producteurs'),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/market/home');
              },
              child: const Text('Marché'),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/forum/home');
              },
              child: const Text('Forum'),
            ),
          ],
        ),
      ),
    );
  }
}
