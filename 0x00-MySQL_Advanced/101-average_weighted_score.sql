-- Create a stored procedure ComputeAverageWeightedScoreForUsers
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight INT;
    DECLARE average FLOAT;
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    OPEN user_cursor;
    
    read_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        -- Calculate the total weighted score and total weight for the user
        SELECT SUM(c.score * p.weight), SUM(p.weight) INTO total_weighted_score, total_weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;
        
        -- Calculate the average weighted score
        SET average = total_weighted_score / total_weight;
        
        -- Update the user's average_score
        UPDATE users
        SET average_score = average
        WHERE id = user_id;
    END LOOP;
    
    CLOSE user_cursor;
END$$
DELIMITER ;