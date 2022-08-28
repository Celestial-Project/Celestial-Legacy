import { spawn } from 'child_process'

export default getResponse = () => {

    const bot_response = spawn('python', ['sensor.py', 'How are you?'])
    const response: string[] = []

    bot_response.stdout.on('data', (res: any) => {
        // convert Buffer object to Float
        response.push(res);
        console.log(response);
    });

    return response
}